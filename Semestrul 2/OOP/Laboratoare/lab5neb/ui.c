#include <stdio.h>
#include "tests.h"
#include <stdlib.h>
#include "controller.h"
#include "oferta.h"

void printMenu() {
	/* Printeaza meniul */
    printf("1. Adaugare oferta\n2. Actualizare oferta\n");
    printf("3. Sterge oferta\n4. Vizualizare oferte ordonat dupa pret, destinatie (crescator/descrescator)\n");
    printf("5. Vizualizare oferte filtrate dupa un criteriu (destinatie, tip, pret, data)\n6. Tipareste toate\n7. Undo\n0. Iesire\n");
}

void testAll() {
	/* Ruleaza toate testele */
	testCopyList();
    testAddService();
    testFindService();
    testModifyService();
    testDeleteService();
    testareaFilter();
    testtipFilter();
    testpretFilter();
	testadressFilter();
    testSortByPrice();
    testSortByType();
    testCreateOferta();
    testEsteAdresaValida();
    testValideazaOferta();
    testResize();
	testUndo();
}

void printAllOferte(MyList* v) {
	/* Afiseaza toate ofertele
	 * Parametri:
	 * v - pointer la lista de oferte (MyList*).
	 */
    if (v->length == 0)
        printf("Nu exista oferte.\n");
    else {
        printf("Ofertele curente sunt:\n");
        for (int i = 0; i < size(v); i++)
        {
            Oferta* o = get(v, i);
            printf("ID: %d | Tip: %s | Suprafata: %d | Adresa : %s | Pret: %d\n",
                o->id, o->tip, o->suprafata, o->adresa, o->pret);
        }
    }
}

void uiAdd(MyList* v, MyList* undo_list) {
    /* Adauga o oferta
     * Parametri:
     * v - pointer la lista de oferte (MyList*).
     * undo_list - lista de oferte anterioara (MyList*).
     */
    int id, pret, suprafata;
    char* tip = (char*)malloc(30 * sizeof(char));
    char* adresa = (char*)malloc(30 * sizeof(char));

    printf("Introduceti id-ul ofertei pentru adaugare: ");
    scanf("%d", &id);

    printf("Tipul ofertei este (apartament, casa, teren): ");
    scanf("%s", tip);

    printf("Suprafata este: ");
    scanf("%d", &suprafata);

    printf("Adresa este: ");
    scanf("%s", adresa);

    printf("Pretul este: ");
    scanf("%d", &pret);
    while (getchar() != '\n');
    int succes = addOferta(v, undo_list, id, tip, suprafata, adresa, pret);

    if (succes == 1) {
        printf("Oferta adaugata cu succes.\n");
    }
    else {
        if (succes == 0)
            printf("Eroare: ID-ul ofertei trebuie sa fie unic.\n");
        else
            if (succes == 2)
                printf("Eroare: Tipul ofertei trebuie sa fie 'teren', 'casa' sau 'apartament'.\n");
            else if (succes == 3)
                printf("Eroare: Suprafata trebuie sa fie un numar pozitiv.\n");
            else if (succes == 4)
                printf("Eroare: Adresa nu poate sa fie goala.\n");
            else if (succes == 5)
                printf("Eroare: Pretul trebuie sa fie un numar pozitiv.\n");
    }

    free(tip);
    free(adresa);
}

void uiModify(MyList* v, MyList* undo_list) {
	/* Modifica o oferta
	 * Parametri:
	 * v - pointer la lista de oferte (MyList*).
	 * undo_list - lista de oferte anterioara (MyList*).
	 */
    int id, pret_nou,suprafata_noua;
    char* tip_nou = (char*)malloc(30 * sizeof(char));
    char* adresa_noua = (char*)malloc(30 * sizeof(char));

    printf("Introduceti id-ul ofertei pentru modificare: ");
    scanf("%d", &id);

    printf("Tipul ofertei este (apartament, casa, teren): ");
    scanf("%s", tip_nou);

    printf("Suprafata este: ");
    scanf("%d", &suprafata_noua);

    printf("Adresa este: ");
    scanf("%s", adresa_noua);

    printf("Pretul este: ");
    scanf("%d", &pret_nou);
    while (getchar() != '\n');

    int succes = modifyOferta(v, undo_list, id, tip_nou, suprafata_noua, adresa_noua, pret_nou);
    if (succes == 1)
    {
        printf("Oferta modificata cu succes.\n");
    }
	if (succes == 0)
	{
	    printf("ID invalid.\n");
	}

	if (succes == 2)
	{
	    printf("Eroare: Tipul ofertei trebuie sa fie 'casa', 'teren' sau 'apartament'.\n");
	}

	if (succes == 3)
	{
	    printf("Eroare: Suprafata trebuie sa fie un numar pozitiv.\n");
	}

	if (succes == 4)
	{
		printf("Eroare: Adresa trebuie sa fie nevida.\n");
	}

	if (succes == 5)
	{
		printf("Eroare: Pretul trebuie sa fie un numar pozitiv.\n");
	}

	free(tip_nou);
	free(adresa_noua);
}

void uiDelete(MyList* v, MyList* undo_list) {
	/* Sterge o oferta
	 * Parametri:
	 * v - pointer la lista de oferte (MyList*).
	 * undo_list - lista de oferte anterioara (MyList*).
	 */
    int id;
    printf("Introduceti id-ul ofertei pe care doriti sa o stergeti: ");
    scanf("%d", &id);
    while (getchar() != '\n');

    int succes = deleteOferta(v, undo_list, id);
    if (succes)
        printf("Oferta stearsa cu succes.\n");
    else
        printf("ID invalid.\n");
}

void uiSort(MyList* v) {
	/* Sorteaza ofertele dupa un criteriu si o ordine specificata
	 * Parametri:
	 * v - pointer la lista de oferte (MyList*).
	 */
    int criteriu, ordine;

    printf("Alegeti criteriul de sortare:\n1. Pret\n2. Destinatie\n");
    scanf("%d", &criteriu);

    printf("Alegeti ordinea:\n1. Crescator\n2. Descrescator\n");
    scanf("%d", &ordine);
    while (getchar() != '\n');

    if ((criteriu != 1 && criteriu != 2) || (ordine != 1 && ordine != 2)) {
        printf("Optiune invalida!\n");
        return;
    }

    sortOferte(v, criteriu, ordine);
    printf("Sortare realizata cu succes!\n");
    printAllOferte(v);
}

void uiFilter(MyList* v) {
	/* Filtreaza ofertele dupa un criteriu specificat
	 * Parametri:
	 * v - pointer la lista de oferte (MyList*).
	 */
    int t, pret,suprafata;
    char tip[30], adresa[30];

    printf("Alegeti tipul filtrarii (1.Suprafata | 2.Tip | 3.Pret | 4. Adresa ): ");
    scanf("%d", &t);
    while (getchar() != '\n');

    if (t == 1) {
        printf("Suprafata este: ");
        scanf("%d", &suprafata);
        MyList* filteredList = areaFilter(v, suprafata);
        printAllOferte(filteredList);
    }
    if (t == 2) {
        printf("Tipul este: ");
        scanf("%29[^\n]", tip);
        MyList* filteredList = tipFilter(v, tip);
        printAllOferte(filteredList);
    }
    if (t == 3) {
        printf("Pretul este: ");
        scanf("%d", &pret);
        MyList* filteredList = pretFilter(v, pret);
        printAllOferte(filteredList);
    }
	if (t == 4) {
		printf("Adresa este: ");
        scanf("%29[^\n]", adresa);
		MyList* filteredList = adressFilter(v, adresa);
		printAllOferte(filteredList);
	}
	if (t!=1 && t!=2 && t!=3 && t!=4) {
		printf("Optiune invalida!\n");
	}
}

void uiStatistica(MyList* v) {
    if (v == NULL || v->length == 0) {
        printf("Nu exista oferte disponibile pentru statistica.\n");
        return;
    }

    MyList* list_statistica = statistica(v);

    printf("\n Statistica ofertelor dupa pret:\n");

    printf("\n Interval mic:\n");
    MyList* List1 = (MyList*)get(list_statistica, 0);
    printAllOferte(List1);

    printf("\n Interval mediu:\n");
    MyList* List2 = (MyList*)get(list_statistica, 1);
    printAllOferte(List2);

    printf("\n Interval mare:\n");
    MyList* List3 = (MyList*)get(list_statistica, 2);
    printAllOferte(List3);

    // Eliberare memorie
    destroy(list_statistica, destroyOfertaLista);
}

void run() {
	/* Ruleaza meniul */
    MyList* oferteList = createEmpty();
	MyList* undo_list = createEmpty();
    int running = 1;
    while (running) {
        printMenu();
        char cmd;
        printf("Comanda este: ");
        scanf("%c", &cmd);
        while (getchar() != '\n');
        switch (cmd) {
        case '1':
            uiAdd(oferteList, undo_list);
            break;
        case '2':
            uiModify(oferteList, undo_list);
            break;
        case '3':
            uiDelete(oferteList, undo_list);
            break;
        case '5':
            uiFilter(oferteList);
            break;
        case '4':
            uiSort(oferteList);
            break;
        case '6':
            printAllOferte(oferteList);
            break;
        case '7':
            if (undo(&oferteList, undo_list) == 0)
            {
                printf("Nu sunt operatii precedente.\n");
            }
            else
            {
                printf("Undo reusit\n");
            }
			break;
        case '8':
            uiStatistica(oferteList);
            break;

        case '0':
            running = 0;
            destroy(oferteList, (void (*)(void*))destroyOferta);
            destroy(undo_list, destroyOfertaLista);
            break;
        default:
            printf("Comanda invalida!\n");
        }
    }
}
