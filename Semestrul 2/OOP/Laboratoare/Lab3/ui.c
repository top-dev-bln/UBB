//
// Created by Balan Andrei Daniel on 13.03.2025.
//
#include "ui.h"
#include "service.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void get_opt(char* opt) {
    printf("1. Adauga masina\n");
    printf("2. Actualizare masina existenta\n");
    printf("3. Inchiriere masina/returnare masina\n");
    printf("4. Vizualizare masini dupa un criteriu dat (categorie, model)\n");
    printf("5. Sortarea masinilor dupa: model sau categorie (crescator/descrescator)\n");
    printf("e. Exit\n");
    printf("-----------------------------------------------------\n");
    printf(">>>> ");

    if (scanf(" %c", opt) != 1) {
        printf("Invalid input\n");
    }

    int ch;
    while ((ch = getchar()) != '\n' && ch != EOF) {}
    system("clear");
}

void run() {
    Repo repo;
    initRepo(&repo);

    char opt;
    bool running = true;
    while (running) {
        get_opt(&opt);

        switch (opt) {
            case '1': {
                char nr_inmatriculare[MAX_LEN], model[MAX_LEN], categorie[MAX_LEN];
                printf("Introduceti numarul de inmatriculare: ");
                scanf(" %49s", nr_inmatriculare);
                printf("Introduceti modelul: ");
                scanf(" %49s", model);
                printf("Introduceti categoria: ");
                scanf(" %49s", categorie);

                if (adaugaMasinaService(&repo, nr_inmatriculare, model, categorie)) {
                    printf("Masina adaugata cu succes! Lista actualizata:\n");
                    afisareToateMasinile(&repo);
                } else {
                    printf("Eroare: Nu s-a putut adauga masina!\n");
                }
                break;
            }
            case '2': {
                char nr_inmatriculare[MAX_LEN], model_nou[MAX_LEN], categorie_noua[MAX_LEN];
                printf("Actualizare masina existenta\n");
                printf("Introduceti numarul de inmatriculare al masinii de actualizat: ");
                scanf(" %49s", nr_inmatriculare);

                int index = cautaMasinaDupaInmatriculare(&repo, nr_inmatriculare);
                if (index == -1) {
                    printf("Eroare: Masina cu numarul %s nu exista!\n", nr_inmatriculare);
                    break;
                }

                printf("Introduceti noul model: ");
                scanf(" %49s", model_nou);
                printf("Introduceti noua categorie: ");
                scanf(" %49s", categorie_noua);

                if (actualizareMasinaService(&repo, nr_inmatriculare, model_nou, categorie_noua)) {
                    printf("Masina actualizata cu succes! Lista actualizata:\n");
                    afisareToateMasinile(&repo);
                } else {
                    printf("Eroare: Nu s-a putut actualiza masina!\n");
                }
                break;
            }
            case '3': {
                printf("Inchiriere masina/returnare masina\n");
                char nr_inmatriculare[MAX_LEN];

                if (afisareToateMasinile(&repo)) {
                    printf("Introduceti numarul de inmatriculare al masinii de inchiriat|returnat: ");
                    scanf(" %49s", nr_inmatriculare);
                    int index = cautaMasinaDupaInmatriculare(&repo, nr_inmatriculare);
                    if (index == -1) {
                        printf("Eroare: Masina cu numarul %s nu exista!\n", nr_inmatriculare);
                        break;
                    }

                    inchiriereMasinaService(&repo, nr_inmatriculare);
                }
                printf("Masina cu numarul de inmatriculare %s a fost inchiriata cu succes!\n", nr_inmatriculare);
                break;
            }

            case '4':
                printf("Vizualizare masini dupa un criteriu dat (categorie, model)\n");
                printf("1. Filtrare dupa categorie\n");
                printf("2. Filtrare dupa model\n");
                printf("Alegeti optiunea (1/2): ");
                char subOpt;
                scanf(" %c", &subOpt);
                if (subOpt != '1' && subOpt != '2') {
                    printf("Optiune invalida!\n");
                    break;
                }
                char filtru[MAX_LEN];
                printf("Introduceti criteriul de filtrare: ");
                scanf(" %49s", filtru);


                Masina filtered[MAX_MASINI];
            int count = filtrare(&repo,subOpt, filtru, filtered);

            if (count == 0) {
                printf("Nu exista masini care sa satisfaca criteriul de filtrare!\n");
            } else {

                for (int i = 0; i < count; i++) {
                    afisareMasina(&filtered[i]);
                }
            }


                break;
            case '5': {
                printf("Sortare masini dupa:\n");
                printf("1. Model\n");
                printf("2. Categorie\n");
                printf("Alegeti optiunea (1/2): ");

                char subOpt;
                scanf(" %c", &subOpt);
                if (subOpt != '1' && subOpt != '2') {
                    printf("Optiune invalida!\n");
                    break;
                }

                printf("Ordine sortare:\n");
                printf("1. Crescator\n");
                printf("2. Descrescator\n");
                printf("Alegeti optiunea (1/2): ");

                char ordine;
                scanf(" %c", &ordine);
                if (ordine != '1' && ordine != '2') {
                    printf("Optiune invalida!\n");
                    break;
                }

                Masina sorted[MAX_MASINI];
                int count = sortareMasini(&repo, subOpt, ordine, sorted);

                if (count == 0) {
                    printf("Nu exista masini de afisat!\n");
                } else {
                    printf("Masini sortate:\n");
                    for (int i = 0; i < count; i++) {
                        afisareMasina(&sorted[i]);
                    }
                }
                break;
            }
            case 'e':
                running = false;
                break;
            default:
                printf("Optiune invalida!\n");
                break;
        }
    }
}