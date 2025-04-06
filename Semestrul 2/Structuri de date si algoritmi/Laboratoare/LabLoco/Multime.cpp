#include "Multime.h"
#include "IteratorMultime.h"

#include <iostream>
using namespace std;
#define OFFSET 999999
#define MAX_ELEM 100000

Multime::Multime() {
	//initializeaza multimea
	//Θ(n)
	for (int i = 0; i < MAX_ELEM+OFFSET; i++) {
		v[i] = false;
	}
	dimensiune = 0;
}

bool Multime::adauga(TElem elem) {
	//primeste un element si il adauga in multime daca nu exista deja
	//input TElem un element
	// returneaza true daca elementul a fost adaugat, false altfel
	// Complexitate Θ(1)
	if (!cauta(elem)) {
		v[elem + OFFSET] = true;
		dimensiune++;
		return true;
	}
	return false;
}

bool Multime::sterge(TElem elem) {
	//cauta un element si il sterge din multime daca exista
	//input TElem un element
	// returneaza true daca elementul a fost sters, false altfel
	// Complexitate Θ(1)
	if (cauta(elem)) {
		v[elem + OFFSET] = false;
		dimensiune--;
		return true;
	}
	return false;
}

bool Multime::cauta(TElem elem) const {
	//cauta un element in multime
	//input TElem un element
	// returneaza true daca elementul exista, false altfel
	// Complexitate Θ(1)
	if (elem + OFFSET < 0 || elem + OFFSET >= MAX_ELEM + OFFSET) return false;
	return v[elem + OFFSET];
}

int Multime::dim() const {
	//returneaza numarul de elemente din multime
	// Complexitate Θ(1)
	return dimensiune;
}

bool Multime::vida() const {
	//verifica daca multimea e vida
	// Complexitate Θ(1)
	return dimensiune == 0;
}



void Multime::filtreaza(Conditie cond) {
	//elimina elementele care nu respecta o conditie
	//input Conditie , o functie booleana care verifica conditia
	// Complexitate Θ(n)
	for (int i = 0; i < MAX_ELEM + OFFSET; i++) {
		int elem = i - OFFSET;
		if (v[i] && !cond(elem)) {
			v[i] = false;
			dimensiune--;
		}
	}
}

IteratorMultime Multime::iterator() const {
	//returneaza un iterator pe multime
	return IteratorMultime(*this);
}
