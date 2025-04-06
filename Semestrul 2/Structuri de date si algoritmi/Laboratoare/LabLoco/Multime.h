#pragma once

#include "IteratorMultime.h"

#define OFFSET 999999
#define MAX_ELEM 100000


typedef int TElem;
typedef bool (*Conditie)(TElem);


class Multime {
	friend class IteratorMultime;

private:
	bool v[MAX_ELEM+OFFSET]{};
	int dimensiune;

public:

	Multime();




	bool adauga(TElem e);

	bool sterge(TElem e);

	bool cauta(TElem elem) const;

	int dim() const;

	bool vida() const;

	void filtreaza(Conditie cond);

	IteratorMultime iterator() const;


};
