#include "IteratorMultime.h"
#include "Multime.h"
#include <stdexcept>


IteratorMultime::IteratorMultime(const Multime& m) : multime(m) {
	prim();
}


void IteratorMultime::prim() {
	curent = 0;
	while ( curent < MAX_ELEM+OFFSET && !multime.v[curent]) {
		curent++;
	}
}


void IteratorMultime::urmator() {
	if (!valid()) {
		throw std::runtime_error("Invalid iterator");
	}
	curent++;
	while (curent< MAX_ELEM+OFFSET && !multime.v[curent]) {
		curent++;
	}
}

bool IteratorMultime::valid() const {
	return curent < MAX_ELEM+OFFSET;
}

TElem IteratorMultime::element() const {
	if (!valid()) {
		throw std::runtime_error("Invalid iterator");
	}
	return curent-OFFSET;
}
