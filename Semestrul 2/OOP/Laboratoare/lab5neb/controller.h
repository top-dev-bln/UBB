#pragma once
#include "repo.h"

//Adauga o oferta
int addOferta(MyList* v, MyList* undo_list, int id, char* tip, int suprafata, char* adresa, int pret);

//Gaseste o oferta dupa un id dat
int findOferta(MyList* v, int id);

//Modifica o oferta
int modifyOferta(MyList* v, MyList* undo_list, int id, char* tip_nou, int suprafata_noua, char* adresa_noua, int pret_nou);

//Sterge o oferta
int deleteOferta(MyList* v, MyList* undo_list, int id);

//Filtreaza dupa suprafata
MyList* areaFilter(MyList* v, int suprafata);

//Filtreaza dupa tip
MyList* tipFilter(MyList* v, char* tip);

//Filtrare dupa pret
MyList* pretFilter(MyList* v, int pret);

MyList* adressFilter(MyList* v, char* adresa);

void sortOferte(MyList* v, int criteriu, int ordine);

//Functie de undo
int undo(MyList** v, MyList* undo_list);

MyList* statistica(MyList* v);

