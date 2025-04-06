#include "tests.h"
#include <assert.h>
#include <string.h>
#include "controller.h"
#include "repo.h"
#include "oferta.h"

void testCopyList() {

	MyList* v1 = createEmpty();
	add(v1, createOferta(1, "casa", 100, "Ploiesti,nr.23", 15000));
	add(v1, createOferta(2, "apartament", 100, "Ploiesti,nr.23", 18000));

	assert(size(v1) == 2);
	MyList* v2 = copyList(v1, copyOferta); 

	assert(size(v2) == 2);
	Oferta* o = get(v2, 0);
	assert(strcmp(o->adresa, "Ploiesti,nr.23") == 0);

	destroy(v1, (void (*)(void*))destroyOferta);
	destroy(v2, (void (*)(void*))destroyOferta);
}

void testAddService() {

	MyList* v = createEmpty();
	MyList* undo_list = createEmpty();
	assert(addOferta(v, undo_list, 1, "casa", 100, "Ploiesti,nr.23", 15000) == 1);
	assert(addOferta(v, undo_list, 1, "casa", 100, "Ploiesti,nr.23", 12000) == 0);

	assert(size(v) == 1);
	Oferta* o = get(v, 0);

	assert(o->id == 1);
	assert(strcmp(o->tip, "casa") == 0);
	assert(o->suprafata== 100);
	assert(strcmp(o->adresa, "Ploiesti,nr.23") == 0);
	assert(o->pret == 15000);

	destroy(v, (void (*)(void*))destroyOferta);
	destroy(undo_list, destroyOfertaLista);
}

void testFindService() {

	MyList* v = createEmpty();
	MyList* undo_list = createEmpty();
	int succes1 = addOferta(v, undo_list, 1, "casa", 100, "Ploiesti,nr.23", 15000);
	assert(succes1 == 1);

	int succes2 = addOferta(v, undo_list, 2, "apartament", 100, "Ploiesti,nr.23",15000);
	assert(succes2 == 1);

	int succes3 = addOferta(v, undo_list, 3, "teren", 100, "Ploiesti,nr.23", 15000);
	assert(succes3 == 1);

	assert(size(v) == 3);
	int poz = findOferta(v, 2);

	assert(poz == 1);

	destroy(v, (void (*)(void*))destroyOferta);
	destroy(undo_list, destroyOfertaLista);
}

void testModifyService() {

	MyList* v = createEmpty();
	MyList* undo_list = createEmpty();
	int succes1 = addOferta(v, undo_list, 1, "casa", 100, "Ploiesti,nr.23", 15000);
	assert(succes1 == 1);

	int succes2 = addOferta(v, undo_list, 2, "apartament", 100, "Ploiesti,nr.23", 15000);
	assert(succes2 == 1);

	int succes3 = addOferta(v, undo_list, 3, "teren", 100, "Ploiesti,nr.23", 15000);
	assert(succes3 == 1);

	assert(size(v) == 3);
	int mod_of1 = modifyOferta(v, undo_list, 2, "apartament", 100, "Stejarului,nr.101", 18000);
	assert(mod_of1 == 1);

	int mod_of2 = modifyOferta(v, undo_list, 4, "apartament", 100, "Stejarului,nr.101", 18000);
	assert(mod_of2 == 0);

	destroy(v, (void (*)(void*))destroyOferta);
	destroy(undo_list, destroyOfertaLista);
}

void testDeleteService() {

	MyList* v = createEmpty();
	MyList* undo_list = createEmpty();
	int succes1 = addOferta(v, undo_list, 1, "casa", 100, "Ploiesti,nr.23", 15000);
	assert(succes1 == 1);

	int succes2 = addOferta(v, undo_list, 2, "apartament", 100, "Ploiesti,nr.23", 15000);
	assert(succes2 == 1);

	int succes3 = addOferta(v, undo_list, 3, "teren", 100, "Ploiesti,nr.23", 15000);
	assert(succes3 == 1);

	assert(size(v) == 3);
	int succes_del1 = deleteOferta(v, undo_list, 2);
	assert(succes_del1 == 1);
	int succes_del2 = deleteOferta(v, undo_list, 5);
	assert(succes_del2 == 0);
	destroy(v, (void (*)(void*))destroyOferta);
	destroy(undo_list, destroyOfertaLista);
}

void testareaFilter() {

	MyList* v = createEmpty();
	MyList* undo_list = createEmpty();
	int succes1 = addOferta(v, undo_list, 1, "casa", 100, "Ploiesti,nr.23", 15000);
	assert(succes1 == 1);

	int succes2 = addOferta(v, undo_list, 2, "apartament", 100, "Ploiesti,nr.23", 15000);
	assert(succes2 == 1);

	int succes3 = addOferta(v, undo_list, 3, "teren", 200, "Ploiesti,nr.23", 15000);
	assert(succes3 == 1);

	assert(size(v) == 3);
	MyList* filteredList = areaFilter(v, 100);
	assert(size(filteredList) == 2);
	destroy(filteredList, (void (*)(void*))destroyOferta);

	filteredList = areaFilter(v, -1);
	assert(size(filteredList) == 3);
	destroy(filteredList, (void (*)(void*))destroyOferta);

	destroy(v, (void (*)(void*))destroyOferta);
	destroy(undo_list, destroyOfertaLista);
}

void  testtipFilter() {

	MyList* v = createEmpty();
	MyList* undo_list = createEmpty();

	int succes1 = addOferta(v, undo_list, 1, "teren", 100, "Ploiesti,nr.23", 15000);
	assert(succes1 == 1);

	int succes2 = addOferta(v, undo_list, 2, "casa", 100, "Ploiesti,nr.23", 15000);
	assert(succes2 == 1);

	int succes3 = addOferta(v, undo_list, 3, "teren", 200, "Ploiesti,nr.23", 15000);
	assert(succes3 == 1);

	assert(size(v) == 3);
	MyList* filteredList = tipFilter(v, "teren");
	assert(size(filteredList) == 2);
	destroy(filteredList, (void (*)(void*))destroyOferta);

	filteredList = tipFilter(v, "");
	assert(size(filteredList) == 3);
	destroy(filteredList, (void (*)(void*))destroyOferta);

	destroy(v, (void (*)(void*))destroyOferta);
	destroy(undo_list, destroyOfertaLista);
}

void testpretFilter() {

	MyList* v = createEmpty();
	MyList* undo_list = createEmpty();

	int succes1 = addOferta(v, undo_list, 1, "casa", 100, "Ploiesti,nr.23", 15000);
	assert(succes1 == 1);

	int succes2 = addOferta(v, undo_list, 2, "apartament", 100, "Ploiesti,nr.23", 15000);
	assert(succes2 == 1);

	int succes3 = addOferta(v, undo_list, 3, "teren", 100, "Ploiesti,nr.23", 158000);
	assert(succes3 == 1);

	assert(size(v) == 3);
	MyList* filteredList = pretFilter(v, 15000);
	assert(size(filteredList) == 2);
	destroy(filteredList, (void (*)(void*))destroyOferta);

	filteredList = pretFilter(v, 0);
	assert(size(filteredList) == 3);
	destroy(filteredList, (void (*)(void*))destroyOferta);

	destroy(v, (void (*)(void*))destroyOferta);
	destroy(undo_list, destroyOfertaLista);
}

void testadressFilter()
{

	MyList* v = createEmpty();
	MyList* undo_list = createEmpty();
	int succes1 = addOferta(v, undo_list, 1, "casa", 100, "Ploiesti,nr.23", 15000);
	assert(succes1 == 1);
	int succes2 = addOferta(v, undo_list, 2, "apartament", 100, "Ploiesti,nr.23", 15000);
	assert(succes2 == 1);
	int succes3 = addOferta(v, undo_list, 3, "teren", 100, "Ploiesti,nr.23", 158000);
	assert(succes3 == 1);
	assert(size(v) == 3);
	MyList* filteredList = adressFilter(v, "Ploiesti,nr.23");
	assert(size(filteredList) == 3);
	destroy(filteredList, (void (*)(void*))destroyOferta);
	filteredList = adressFilter(v, "Ploiesti,nr.8");
	assert(size(filteredList) == 0);
	destroy(filteredList, (void (*)(void*))destroyOferta);

	filteredList = adressFilter(v, "");
	assert(size(filteredList) == 3);
	for (int i = 0; i < filteredList->length; i++)
	{
		Oferta* o = get(filteredList, i);
		assert(strcmp(o->adresa, "Ploiesti,nr.23") == 0);
	}
	destroy(filteredList, (void (*)(void*))destroyOferta);
	destroy(v, (void (*)(void*))destroyOferta);
	destroy(undo_list, destroyOfertaLista);
}

void testSortByPrice() {

	MyList* v = createEmpty();
	MyList* undo_list = createEmpty();
	addOferta(v, undo_list, 1, "casa", 100, "Ploiesti,nr.23", 500);
	addOferta(v, undo_list, 2, "apartament", 200, "Ploiesti,nr.23", 300);
	addOferta(v, undo_list, 3, "teren", 300, "Ploiesti,nr.23", 700);

	sortOferte(v, 1, 1); // Sortare crescătoare după preț
	assert(((Oferta*)get(v, 0))->pret == 300);
	assert(((Oferta*)get(v, 1))->pret == 500);
	assert(((Oferta*)get(v, 2))->pret == 700);

	sortOferte(v, 1, 2); // Sortare descrescătoare după preț
	assert(((Oferta*)get(v, 0))->pret == 700);
	assert(((Oferta*)get(v, 1))->pret == 500);
	assert(((Oferta*)get(v, 2))->pret == 300);


	destroy(v, (void (*)(void*))destroyOferta);
	destroy(undo_list, destroyOfertaLista);
}

void testSortByType() {

	MyList* v = createEmpty();
	MyList* undo_list = createEmpty();
	addOferta(v, undo_list, 1, "casa", 100, "Ploiesti,nr.23", 500);
	addOferta(v, undo_list, 2, "apartament", 200, "Ploiesti,nr.23", 300);
	addOferta(v, undo_list, 3, "teren", 300, "Ploiesti,nr.23", 700);

	sortOferte(v, 2, 1); // Sortare crescătoare după tip

	assert(((Oferta*)get(v, 0))->pret == 300);
	assert(((Oferta*)get(v, 1))->pret == 500);
	assert(((Oferta*)get(v, 2))->pret == 700);


	destroy(v, (void (*)(void*))destroyOferta);
	destroy(undo_list, destroyOfertaLista);
}


void testCreateOferta() {

	Oferta* o = createOferta(1, "casa", 100, "Ploiesti,nr.23", 500);
	assert(o->id == 1);
	assert(strcmp(o->tip, "casa") == 0);
	assert(o->suprafata == 100);
	assert(strcmp(o->adresa, "Ploiesti,nr.23") == 0);
	assert(o->pret == 500);

	destroyOferta(o);
}

void testEsteAdresaValida() {
	assert(esteAdresaValida("Lalelelor,nr.3") == 1);
	assert(esteAdresaValida("StradaMare,nr.10") == 1);
	assert(esteAdresaValida("123,nr.4") == 0);
	assert(esteAdresaValida("Strada,nr.") == 0);
	assert(esteAdresaValida("PiataUnirii,nr.5") == 1);
}
void testValideazaOferta() {

	Oferta* o1 = createOferta(1, "casa", 100, "Ploiesti,nr.23", 500);
	assert(valideazaOferta(o1) == 1);
	destroyOferta(o1);

	Oferta* o2 = createOferta(2, "apartment", 100, "Mihai Viteazu,nr.15", 600); // Tip invalid
	assert(valideazaOferta(o2) == 2);
	destroyOferta(o2);

	Oferta* o3 = createOferta(3, "teren", -100, "Stejarului,nr.101", 400); // Suprafata invalida
	assert(valideazaOferta(o3) == 3);
	destroyOferta(o3);

	Oferta* o4 = createOferta(4, "casa",200, "40", 700); // Data invalida
	assert(valideazaOferta(o4) == 4);
	destroyOferta(o4);

	Oferta* o5 = createOferta(5, "apartament", 300, "Eroilor,nr.2", -100); // Pret invalid
	assert(valideazaOferta(o5) == 5);
	destroyOferta(o5);
}

void testResize() {

	MyList* v = createEmpty();

	for (int i = 0; i < 20; i++) {
		Oferta* o = createOferta(i, "casa",100, "Eroilor,nr.2", 15000);
		add(v, o);
	}

	assert(v->capacity == 20); 

	assert(size(v) == 20);

	for (int i = 0; i < 20; i++) {
		Oferta* o = get(v, i);
		assert(o->id == i);
		assert(strcmp(o->tip, "casa") == 0);
		assert(o->suprafata== 100);
		assert(strcmp(o->adresa, "Eroilor,nr.2") == 0);
		assert(o->pret == 15000);
	}
	destroy(v, (void (*)(void*))destroyOferta);
}

void testUndo()
{

	MyList* v = createEmpty();
	MyList* undo_list = createEmpty();

	assert(undo(&v, undo_list) == 0);

	addOferta(v, undo_list, 1, "casa", 100, "Eroilor,nr.2", 500);
	addOferta(v, undo_list, 2, "apartament", 200, "Stejarului,nr.101", 300);
	addOferta(v, undo_list, 3, "teren", 300, "Eroilor,nr.2", 700);
	assert(undo(&v, undo_list) == 1);
	assert(size(v) == 2);

	Oferta* o1 = get(v, 0);
	assert(o1->id == 1);
	assert(strcmp(o1->tip, "casa") == 0);
	assert(o1->suprafata == 100);
	assert(strcmp(o1->adresa, "Eroilor,nr.2") == 0);
	assert(o1->pret == 500);
	Oferta* o2 = get(v, 1);
	assert(o2->id == 2);
	assert(strcmp(o2->tip, "apartament") == 0);
	assert(o2->suprafata == 200);
	assert(strcmp(o2->adresa, "Stejarului,nr.101") == 0);
	assert(o2->pret == 300);
	destroy(v, (void (*)(void*))destroyOferta);
	destroy(undo_list, destroyOfertaLista);
}
