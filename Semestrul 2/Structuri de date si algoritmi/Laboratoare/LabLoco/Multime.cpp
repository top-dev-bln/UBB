#include "Multime.h"
#include "IteratorMultime.h"

#include <iostream>
using namespace std;
#define OFFSET 999999
#define MAX_ELEM 100000

Multime::Multime() {
	for (int i = 0; i < MAX_ELEM+OFFSET; i++) {
		v[i] = false;
	}
	dimensiune = 0;
}

bool Multime::adauga(TElem elem) {
	if (elem + OFFSET < 0 || elem + OFFSET >= MAX_ELEM + OFFSET) return false;
	if (!v[elem + OFFSET]) {
		v[elem + OFFSET] = true;
		dimensiune++;
		return true;
	}
	return false;
}

bool Multime::sterge(TElem elem) {
	if (elem + OFFSET < 0 || elem + OFFSET >= MAX_ELEM + OFFSET) return false;
	if (v[elem + OFFSET]) {
		v[elem + OFFSET] = false;
		dimensiune--;
		return true;
	}
	return false;
}

bool Multime::cauta(TElem elem) const {
	if (elem + OFFSET < 0 || elem + OFFSET >= MAX_ELEM + OFFSET) return false;
	return v[elem + OFFSET];
}

int Multime::dim() const {
	return dimensiune;
}

bool Multime::vida() const {
	return dimensiune == 0;
}

IteratorMultime Multime::iterator() const {
	return IteratorMultime(*this);
}
