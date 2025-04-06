#include "IteratorMultime.h"
#include "Multime.h"
#include <stdexcept>


IteratorMultime::IteratorMultime(const Multime& m) : multime(m) {
	//constructor iterator pentru o multime
	prim();
}


void IteratorMultime::prim() {
	//muta iteratorul la primul element
	// Complexitate O(n) sau
	curent = 0;
	while ( curent < MAX_ELEM+OFFSET && !multime.v[curent]) {
		curent++;
	}
}


void IteratorMultime::urmator() {
	//muta iteratorul pe urmatorul element
	// Complexitate Θ(1)
	if (!valid()) {
		throw std::runtime_error("Invalid iterator");
	}
	curent++;
	while (curent< MAX_ELEM+OFFSET && !multime.v[curent]) {
		curent++;
	}
}

bool IteratorMultime::valid() const {
	//verifica daca iteratorul e valid
	// Complexitate Θ(1)
	return curent < MAX_ELEM+OFFSET;
}

TElem IteratorMultime::element() const {
	//returneaza elementul curent din iterator
	// Complexitate Θ(1)
	if (!valid()) {
		throw std::runtime_error("Invalid iterator");
	}
	return curent-OFFSET;
}
