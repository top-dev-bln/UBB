//
// Created by Balan Andrei Daniel on 13.03.2025.
//

#include "repo.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void initRepo(Repo *repo) {
    //input : repo - pointer la Repository
    //output : -
    //Functia initializeaza un Repository
    repo->dim = 0;
    repo->capacitate = 10;
    repo->masini = (Masina*)malloc(repo->capacitate * sizeof(Masina));
}

int cautaMasinaDupaInmatriculare(const Repo *repo, const char *nr_inmatriculare) {
    //input : repo - pointer la Repository, nr_inmatriculare - pointer la sir de caractere
    //output : returneaza indexul masinii cu numarul de inmatriculare dat sau -1 daca masina nu a fost gasita
    for (int i = 0; i < repo->dim; i++) {
        if (strcmp(repo->masini[i].nr_inmatriculare, nr_inmatriculare) == 0) {
            return i;
        }
    }
    return -1;
}



int actualizareMasinaRepo(Repo *repo, const char *nr_inmatriculare, const Masina *m_nou) {
    // input: repo - pointer la Repository, nr_inmatriculare - pointer la numărul de înmatriculare,
    // m_nou - pointer la obiectul Masina cu datele noi
    // output: returnează 1 dacă mașina a fost actualizată cu succes, 0 altfel


    int index = cautaMasinaDupaInmatriculare(repo, nr_inmatriculare);
    if (index == -1) {
        return 0;
    }

    repo->masini[index] = *m_nou;


    strncpy(repo->masini[index].nr_inmatriculare, nr_inmatriculare, MAX_LEN - 1);
    repo->masini[index].nr_inmatriculare[MAX_LEN - 1] = '\0';

    return 1;


}



int adaugaMasinaRepo(Repo *repo, const Masina *m) {
    //input : repo - pointer la Repository, m - pointer la Masina
    //output : returneaza 1 daca masina a fost adaugata cu succes, 0 altfel
    //Functia adauga o masina in Repository
    if (repo->dim == repo->capacitate) {
        repo->capacitate *= 2;
        repo->masini = (Masina*)realloc(repo->masini, repo->capacitate * sizeof(Masina));

    }
    repo->masini[repo->dim] = *m;
    repo->dim++;
    return 1;
}





void elibereazaRepo(Repo *repo) {
    //input : repo - pointer la Repository
    //output : -
    //Functia elibereaza memoria alocata pentru Repository
    free(repo->masini);
    repo->masini = NULL;
    repo->dim = 0;
    repo->capacitate = 0;
}
