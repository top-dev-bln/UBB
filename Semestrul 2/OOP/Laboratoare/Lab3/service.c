//
// Created by Balan Andrei Daniel on 13.03.2025.
//

#include "service.h"
#include <stdio.h>
#include <string.h>



int actualizareMasinaService(Repo *repo, const char *nr_inmatriculare, const char *model_nou, const char *categorie_noua) {
    //input : repo - pointer la Repository, nr_inmatriculare - pointer la sir de caractere, model_nou - pointer la sir de caractere, categorie_noua - pointer la sir de caractere
    //output : returneaza 1 daca masina a fost actualizata cu succes, 0 altfel,
    //Functia cauta masina cu numarul de inmatriculare dat si o actualizeaza cu datele introduse
    int index = cautaMasinaDupaInmatriculare(repo, nr_inmatriculare);
    if (index == -1) {
        return 0;
    }


    strncpy(repo->masini[index].model, model_nou, MAX_LEN - 1);
    repo->masini[index].model[MAX_LEN - 1] = '\0';
    strncpy(repo->masini[index].categorie, categorie_noua, MAX_LEN - 1);
    repo->masini[index].categorie[MAX_LEN - 1] = '\0';

    return 1;
}
int adaugaMasinaService(Repo *repo, const char *nr_inmatriculare, const char *model, const char *categorie) {
    //input : repo - pointer la Repository, nr_inmatriculare - pointer la sir de caractere, model - pointer la sir de caractere, categorie - pointer la sir de caractere
    //output : returneaza 1 daca masina a fost adaugata cu succes, 0 altfel
    //Functia adauga o masina in Repository

    if (cautaMasinaDupaInmatriculare(repo, nr_inmatriculare) != -1) {
        return 0;
    }

    Masina m;
    creareMasina(&m, nr_inmatriculare, model, categorie);
    return adaugaMasinaRepo(repo, &m);
}
void inchiriereMasinaService(Repo *repo, const char *nr_inmatriculare) {
    //input : repo - pointer la Repository, nr_inmatriculare - pointer la sir de caractere
    //output : -
    //Functia cauta masina cu numarul de inmatriculare dat si schimba statusul de inchiriere
    int index = cautaMasinaDupaInmatriculare(repo, nr_inmatriculare);
    if (index == -1) {
        return;
    }


    repo->masini[index].inchiriata = !repo->masini[index].inchiriata;
}

int filtrare(Repo *repo, char subOpt, const char *filtru, Masina *filtered) {
    //input : repo - pointer la Repository, subOpt - caracter, filtru - pointer la sir de caractere, filtered - pointer la Masina
    //output : returneaza numarul de masini filtrate
    //Functia filtreaza masinile dupa un criteriu dat
    int count = 0;
    for (int i = 0; i < repo->dim; i++) {
        if (subOpt == '1' && strcmp(repo->masini[i].categorie, filtru) == 0) {
            filtered[count++] = repo->masini[i];
        } else if (subOpt == '2' && strcmp(repo->masini[i].model, filtru) == 0) {
            filtered[count++] = repo->masini[i];
        }
    }
    return count;
}


int sortareMasini(Repo *repo, char criteriu, char ordine, Masina *sorted) {
    //input : repo - pointer la Repository, criteriu - caracter, ordine - caracter, sorted - pointer la Masina
    //output : returneaza numarul de masini sortate
    //Functia sorteaza masinile dupa un criteriu dat , lista sortata fiind salvata in sorted
    for (int i = 0; i < repo->dim; i++) {
        sorted[i] = repo->masini[i];
    }

    // Bubble sort
    for (int i = 0; i < repo->dim - 1; i++) {
        for (int j = 0; j < repo->dim - 1 - i; j++) {
            int cmp = 0;


            if (criteriu == '1') {
                cmp = strcmp(sorted[j].model, sorted[j + 1].model);
            } else if (criteriu == '2') {
                cmp = strcmp(sorted[j].categorie, sorted[j + 1].categorie);
            }


            if (ordine == '1') {
                if (cmp > 0) {

                    Masina temp = sorted[j];
                    sorted[j] = sorted[j + 1];
                    sorted[j + 1] = temp;
                }
            } else if (ordine == '2') {
                if (cmp < 0) {
                    Masina temp = sorted[j];
                    sorted[j] = sorted[j + 1];
                    sorted[j + 1] = temp;
                }
            }
        }
    }

    return repo->dim;
}