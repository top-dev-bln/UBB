#include "controller.h"
#include <string.h>
#include <stdlib.h>

#include "oferta.h"
#include "repo.h"

int addOferta(MyList* v, MyList* undo_list, int id, char* tip,int suprafata, char* adresa, int pret) {
	/*
	*Creeaza o oferta noua si o adauga in lista v daca este valida.
	Parametri:
	v – pointer catre lista de oferte (MyList*).
	id – identificator unic al ofertei (int).
	tip – tipul ofertei (mare,munte sau city break) (char*).
	suprafata – locatia ofertei (int).
	adresa – data plecarii (char*).
	pret – pretul ofertei (int).
	Returneaza:
	1 daca oferta a fost adaugata cu succes.
	0 daca oferta este invalida si nu a fost adaugata.
	 */
	add(undo_list, copyList(v, copyOferta));
	if (findOferta(v, id) != -1)
	{
		return 0;
	}
	Oferta* o = createOferta(id, tip, suprafata, adresa, pret);
	int c = valideazaOferta(o);
	if (c == 1)
	{
		add(v, o);
	}
	return c;
}

int findOferta(MyList* v, int id) {
	/*
	*Cauta o oferta cu id-ul specificat in lista v.
	Parametri:
	v – pointer catre lista de oferte (MyList*).
	id – identificatorul unic al ofertei cautate (int).
	Returneaza:
	Pozitia ofertei in lista (int) daca este gasita.
	-1 daca oferta nu exista in lista.
	 */
	int poz_to_delete = -1;
	for (int i = 0; i < v->length; i++) {
		Oferta* o = get(v, i);
		if (id == o->id) {
			poz_to_delete = i;
			break;
		}
	}
	return poz_to_delete;
}

int modifyOferta(MyList* v, MyList* undo_list, int id, char* tip_nou, int suprafata_noua, char* adresa_noua, int pret_nou) {
	/*
	* Modifica datele unei oferte existente cu id-ul specificat.
	Parametri:
	v – pointer catre lista de oferte (MyList*).
	id – identificatorul unic al ofertei care trebuie modificata (int).
	tip_nou – noul tip al ofertei (char*).
	suprafata_noua – noua suprafata (int).
	adresa_noua – noua adresa (char*).
	pret_nou – noul pret al ofertei (int).
	Returneaza:
	1 daca modificarea a fost realizata cu succes.
	0 daca oferta nu a fost gasita si nu s-a modificat nimic.
	 */
	add(undo_list, copyList(v, copyOferta));
	int poz_to_delete = findOferta(v, id);
	if (poz_to_delete != -1) {
		Oferta* ofertaNoua = createOferta(id, tip_nou, suprafata_noua, adresa_noua, pret_nou);
		int valid = valideazaOferta(ofertaNoua);
		if (valid != 1)
		{
			return valid;
		}
		Oferta* o = get(v, poz_to_delete);
		destroyOferta(o);
		setElem(v, poz_to_delete, ofertaNoua);
		return 1;
	}
	return 0;
}

int deleteOferta(MyList* v, MyList* undo_list, int id) {
	/*
	*Sterge o oferta cu id-ul dat din lista v, daca exista.
	Parametri:
	v – pointer catre lista de oferte (MyList*).
	id – identificatorul unic al ofertei de sters (int).
	Returneaza:
	1 daca oferta a fost stearsa cu succes.
	0 daca oferta nu a fost gasita.
	 */
	add(undo_list, copyList(v, copyOferta));
	int poz_to_delete = findOferta(v, id);
	if (poz_to_delete != -1) {
		Oferta* o = delete(v, poz_to_delete);
		destroyOferta(o);
		return 1;
	}
	return 0;
}

MyList* areaFilter(MyList* v, int suprafata) {
	/*
	* Creeaza si returneaza o noua lista de oferte care au aceeasi destinatie ca cea specificata.
	*
	* Parametri:
	* v – pointer catre lista de oferte (MyList*).
	* suprafata – suprafata pe care dorim sa o filtram (char*).
	*
	* Returneaza:
	* O lista noua care contine doar ofertele cu suprafata respectiva.
	* O copie a listei initiale daca suprafata este negativa sau nula.
	*/

	if (suprafata <= 0) {
		return copyList(v, (ElemType(*)(ElemType))copyOferta);
	}

	MyList* filteredList = createEmpty();

	for (int i = 0; i < v->length; i++) {
		Oferta* o = get(v, i);
		if (o != NULL && o->suprafata == suprafata) {
			add(filteredList, createOferta(o->id, o->tip, o->suprafata, o->adresa, o->pret));
		}
	}

	return filteredList;
}


MyList* tipFilter(MyList* v, char* tip) {
	/*
	* Creeaza si returneaza o lista noua cu ofertele care au acelasi tip ca cel specificat.
	*
	* Parametri:
	* v – pointer catre lista de oferte (MyList*).
	* tip – tipul ofertei pentru filtrare (char*).
	*
	* Returneaza:
	* O lista noua care contine doar ofertele cu tipul specificat.
	*/

	if (strcmp(tip, "") == 0) {
		return copyList(v, (ElemType(*)(ElemType))copyOferta);
	}

	MyList* filteredList = createEmpty();

	for (int i = 0; i < v->length; i++) {
		Oferta* o = get(v, i);
		if (o != NULL && strcmp(o->tip, tip) == 0) {
			add(filteredList, createOferta(o->id, o->tip, o->suprafata, o->adresa, o->pret));
		}
	}

	return filteredList;
}


MyList* pretFilter(MyList* v, int pret) {
	/*
	* Creeaza si returneaza o lista noua cu ofertele care au acelasi pret ca cel specificat.
	*
	* Parametri:
	* v – pointer catre lista de oferte (MyList*).
	* pret – pretul ofertei pentru filtrare (int).
	*
	* Returneaza:
	* O lista noua care contine doar ofertele cu pretul specificat.
	* O copie a listei initiale daca pret este negativ sau zero.
	*/

	if (pret <= 0) {
		return copyList(v, (ElemType(*)(ElemType))copyOferta);
	}

	MyList* filteredList = createEmpty();

	for (int i = 0; i < v->length; i++) {
		Oferta* o = get(v, i);
		if (o != NULL && o->pret == pret) {
			add(filteredList, createOferta(o->id, o->tip, o->suprafata, o->adresa, o->pret));
		}
	}

	return filteredList;
}

MyList* adressFilter(MyList* v, char* adresa)
{
	/* Creeaza si returneaza o lista noua cu ofertele care au aceeasi adresa ca cea specificata.
	 * Parametri:
	 * v - pointer catre lista de oferte (MyList*).
	 * adresa - adresa pe care dorim sa o filtram (char*).
	 * Returneaza:
	 * O lista noua care contine doar ofertele cu adresa respectiva.
	 * O copie a listei initiale daca adresa este invalida sau goala.
	 */
	if (esteAdresaValida(adresa) == 0 || adresa == NULL) {
		return copyList(v, (ElemType(*)(ElemType))copyOferta);
	}
	MyList* filteredList = createEmpty();
	for (int i = 0; i < v->length; i++) {
		Oferta* o = get(v, i);
		if (strcmp(o->adresa,adresa) == 0) {
			add(filteredList, createOferta(o->id, o->tip, o->suprafata, o->adresa, o->pret));
		}
	}
	return filteredList;
}


void sortOferte(MyList* v, int criteriu, int ordine) {
	/* Sorteaza lista de oferte dupa un criteriu specificat.
	 * Parametri:
	 * v - pointer catre lista de oferte (MyList*).
	 * criteriu - criteriul de sortare (int).
	 * ordine - ordinea de sortare (int).
	 */
	for (int i = 0; i < v->length - 1; i++) {
		for (int j = i + 1; j < v->length; j++) {
			int conditie = 0;
			Oferta* o1 = get(v, i);
			Oferta* o2 = get(v, j);
			if (criteriu == 1) {
				conditie = (ordine == 1) ? (o1->pret > o2->pret) : (o1->pret < o2->pret);
			}
			else if (criteriu == 2) {
				conditie = (ordine == 1) ? (strcmp(o1->tip, o2->tip) > 0) : (strcmp(o1->tip, o2->tip) < 0);
			}
			if (conditie) {
				setElem(v, i, o2);
				setElem(v, j, o1);
			}
		}
	}
}



int undo(MyList** v, MyList* undo_list) {
	/* Functie de undo care revine la starea anterioara a listei de oferte.
	 * Parametri:
	 * v - pointer catre lista de oferte (MyList**).
	 * undo_list - lista de oferte anterioara (MyList*).
	 * Returneaza:
	 * 1 daca undo a fost realizat cu succes.
	 * 0 daca undo nu a fost realizat.
	 */
	if (size(undo_list) == 0) {
		return 0;
	}
	destroy(*v, (void (*)(void*))destroyOferta); 
	*v = (MyList*)delete(undo_list, size(undo_list) - 1); 
	return 1;
}

MyList* statistica(MyList* v) {
	if (v == NULL || v->length == 0)
		return NULL;

	int pret_min = ((Oferta*)get(v, 0))->pret;
	int pret_max = ((Oferta*)get(v, v->length - 1))->pret;

	MyList* List1 = createEmpty();
	MyList* List2 = createEmpty();
	MyList* List3 = createEmpty();

	for (int i = 0; i < v->length; i++) {
		Oferta* oferta = (Oferta*)get(v, i);
		int pret = oferta->pret;

		if (pret <= pret_min + (pret_max - pret_min) / 3)
			add(List1, copyOferta(oferta));
		else if (pret <= pret_min + 2 * (pret_max - pret_min) / 3)
			add(List2, copyOferta(oferta));
		else
			add(List3, copyOferta(oferta));
	}

	MyList* list_statistica = createEmpty();
	add(list_statistica, List1);
	add(list_statistica, List2);
	add(list_statistica, List3);

	return list_statistica;
}
