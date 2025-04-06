#pragma once
#include "repo.h"

// Afișează meniul principal
void printMenu();

// Rulează toate testele
void testAll();

// Afișează toate ofertele din listă
void printAllOferte(MyList* v);

// Adaugă o ofertă imobiliară prin interfața utilizatorului
void uiAdd(MyList* v, MyList* undo_list);

// Modifică o ofertă imobiliară prin interfața utilizatorului
void uiModify(MyList* v, MyList* undo_list);

// Șterge o ofertă imobiliară prin interfața utilizatorului
void uiDelete(MyList* v, MyList* undo_list);

// Sortează ofertele imobiliare după preț și tip (crescător/descrescător)
void uiSort(MyList* v);

// Filtrează ofertele imobiliare în funcție de criterii (suprafață, tip, preț)
void uiFilter(MyList* v);

void uiStatistica(MyList* v);

// Rulează aplicația
void run();
