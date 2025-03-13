#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct {
    char numar_inmatriculare[15];
    char model[50];
    char categorie[20];
    bool inchiriata; // true = inchiriata, false = disponibila
} Masina;

typedef struct {
    Masina* masini;
    int nr_masini;
    int capacitate;
} ListaMasini;

void init_lista(ListaMasini* lista, int capacitate_initiala) {
    lista->masini = (Masina*)malloc(capacitate_initiala * sizeof(Masina));
    if (lista->masini == NULL) {
        printf("Eroare alocare memorie!\n");
        return;
    }
    lista->nr_masini = 0;
    lista->capacitate = capacitate_initiala;
}

void elibereaza_lista(ListaMasini* lista) {
    free(lista->masini);
    lista->masini = NULL;
    lista->nr_masini = 0;
    lista->capacitate = 0;
}

void adauga_masina(ListaMasini* lista, const char* numar, const char* model, const char* categorie) {
    if (lista->nr_masini >= lista->capacitate) {
        int noua_capacitate = lista->capacitate * 2;
        Masina* masini_noi = (Masina*)realloc(lista->masini, noua_capacitate * sizeof(Masina));
        if (masini_noi == NULL) {
            printf("Eroare alocare memorie!\n");
            return;
        }
        lista->masini = masini_noi;
        lista->capacitate = noua_capacitate;
    }

    Masina* masina = &lista->masini[lista->nr_masini];
    strcpy_s(masina->numar_inmatriculare, sizeof(masina->numar_inmatriculare), numar);
    strcpy_s(masina->model, sizeof(masina->model), model);
    strcpy_s(masina->categorie, sizeof(masina->categorie), categorie);

    masina->inchiriata = false;

    lista->nr_masini++;
    printf("Masina adaugata cu succes!\n");
}

void afiseaza_masini(const ListaMasini* lista) {
    printf("Lista masinilor:\n");
    for (int i = 0; i < lista->nr_masini; i++) {
        printf("%d. %s - %s - %s [%s]\n", i + 1, lista->masini[i].numar_inmatriculare, lista->masini[i].model, lista->masini[i].categorie, lista->masini[i].inchiriata ? "Inchiriata" : "Disponibila");
    }
}

void citeste_string(char* buffer, int dimensiune) {
    fgets(buffer, dimensiune, stdin);
    buffer[strcspn(buffer, "\n")] = 0; // Remove newline character
}

void get_opt(char* opt) {
    printf("1. Adauga masina\n");
    printf("2. Actualizare masina existenta\n");
    printf("3. Inchiriere masina/returnare masina\n");
    printf("4. Vizualizare masini dupa un criteriu dat (categorie, model)\n");
    printf("5. Sortarea masinilor dupa: model sau categorie (crescator/descrescator)\n");
    printf("e. Exit\n");
    printf("-----------------------------------------------------\n");
    printf(">>>> ");

    if (scanf_s(" %c", opt, 1) != 1) {
        printf("Invalid input\n");
    }
    // Consume the newline character left in the buffer
    int ch;
    while ((ch = getchar()) != '\n' && ch != EOF) {
        // Explicitly handle the return value of getchar()
    }
    system("cls");
}

int main() {
    ListaMasini lista;
    init_lista(&lista, 2);

    char opt;
    bool running = true;
    while (running) {
        get_opt(&opt);

        switch (opt) {
        case '1': {
            printf("Adauga masina\n");

            char numar[15];
            char model[50];
            char categorie[20];

            printf("Numar inmatriculare: ");
            citeste_string(numar, sizeof(numar));

            printf("Model: ");
            citeste_string(model, sizeof(model));

            printf("Categorie: ");
            citeste_string(categorie, sizeof(categorie));

            adauga_masina(&lista, numar, model, categorie);

           
			afiseaza_masini(&lista);
            break;
        }
        case '2':
            printf("Actualizare masina existenta\n");
            break;
        case '3':
            printf("Inchiriere masina/returnare masina\n");
            break;
        case '4':
            printf("Vizualizare masini dupa un criteriu dat (categorie, model)\n");
            break;
        case '5':
            printf("Sortarea masinilor dupa: model sau categorie (crescator/descrescator)\n");
            break;
        case 'e':
            running = false;
            break;
        default:
            printf("Optiune invalida!\n");
            break;
        }
    }

    elibereaza_lista(&lista);
    return 0;
}