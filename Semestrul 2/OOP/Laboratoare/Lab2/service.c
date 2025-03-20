//
// Created by Balan Andrei Daniel on 13.03.2025.
//

#include "service.h"
#include <stdio.h>
#include <string.h>



int actualizareMasinaService(Repo *repo, const char *nr_inmatriculare, const char *model_nou, const char *categorie_noua) {
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

    if (cautaMasinaDupaInmatriculare(repo, nr_inmatriculare) != -1) {
        return 0;
    }

    Masina m;
    creareMasina(&m, nr_inmatriculare, model, categorie);
    return adaugaMasinaRepo(repo, &m);
}
void inchiriereMasinaService(Repo *repo, const char *nr_inmatriculare) {
    int index = cautaMasinaDupaInmatriculare(repo, nr_inmatriculare);
    if (index == -1) {
        return;
    }


    repo->masini[index].inchiriata = !repo->masini[index].inchiriata;
}

int filtrare(Repo *repo, char subOpt, const char *filtru, Masina *filtered) {
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

void sortByModel(Masina *sorted, int dim) {
    int swapped = 1;
    while (swapped) {
        swapped = 0;
        for (int i = 0; i < dim - 1; i++) {
            int cmp = strcmp(sorted[i].model, sorted[i + 1].model);

            if (cmp > 0) {
                Masina temp = sorted[i];
                sorted[i] = sorted[i + 1];
                sorted[i + 1] = temp;
                swapped = 1;
            }
        }
    }
}
void sortByCategorie(Masina *sorted, int dim) {
    int swapped = 1;
    while (swapped) {
        swapped = 0;
        for (int i = 0; i < dim - 1; i++) {
            int cmp = strcmp(sorted[i].categorie, sorted[i + 1].categorie);

            if (cmp > 0) {
                Masina temp = sorted[i];
                sorted[i] = sorted[i + 1];
                sorted[i + 1] = temp;
                swapped = 1;
            }
        }
    }
}

int sortareMasini(Repo *repo, char criteriu, char ordine, Masina *sorted) {

    for (int i = 0; i < repo->dim; i++) {
        sorted[i] = repo->masini[i];
    }


    if (criteriu == '1') {
        sortByModel(sorted, repo->dim);
    } else if (criteriu == '2') {
        sortByCategorie(sorted, repo->dim);
    }


    if (ordine == '2') {
        for (int i = 0; i < repo->dim / 2; i++) {
            Masina temp = sorted[i];
            sorted[i] = sorted[repo->dim - i - 1];
            sorted[repo->dim - i - 1] = temp;
        }
    }

    return repo->dim;
}