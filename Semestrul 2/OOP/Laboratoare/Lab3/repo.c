//
// Created by Balan Andrei Daniel on 13.03.2025.
//

#include "repo.h"
#include <stdio.h>
#include <string.h>

void initRepo(Repo *repo) {
    repo->dim = 0;
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
    //input : repo - pointer la Repository, nr_inmatriculare - pointer la sir de caractere, m_nou - pointer la Masina
    //output : returneaza 1 daca masina a fost actualizata cu succes, 0 altfel,
    //Functia cauta masina cu numarul de inmatriculare dat si o actualizeaza cu datele introduse
    int index = cautaMasinaDupaInmatriculare(repo, nr_inmatriculare);
    if (index == -1) {
        return 0; // Ia-o de unde nu-i
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
    if (repo->dim >= MAX_MASINI) {
        return 0;
    }
    repo->masini[repo->dim] = *m;
    repo->dim++;
    return 1;
}

int afisareToateMasinile(const Repo *repo) {
    //input : repo - pointer la Repository
    //output: returneaza 1 daca exista masini in Repository, 0 altfel
    //Functia afiseaza toate masinile din Repository
    if (repo->dim == 0) {
        return 0;
    }
    for (int i = 0; i < repo->dim; i++) {
        afisareMasina(&repo->masini[i]);
    }
    return 1;
}