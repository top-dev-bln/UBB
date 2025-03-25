#pragma once

class Multime;

typedef int TElem;

class IteratorMultime {
	friend class Multime;

private:
	const Multime& multime;
	int curent{};

	IteratorMultime(const Multime& m);

public:

	void prim();

	void urmator();

	bool valid() const;

	TElem element() const;
};