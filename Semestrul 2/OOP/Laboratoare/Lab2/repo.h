//
// Created by Balan Andrei Daniel on 13.03.2025.
//

#ifndef REPO_H
#define REPO_H

#include "masina.h"

#define MAX_MASINI 100

typedef struct {
    Masina masini[MAX_MASINI];
    int dim;
} Repo;

void initRepo(Repo *repo);
int actualizareMasinaRepo(Repo *repo, const char *nr_inmatriculare, const Masina *m_nou);
int cautaMasinaDupaInmatriculare(const Repo *repo, const char *nr_inmatriculare);
int adaugaMasinaRepo(Repo *repo, const Masina *m);
int afisareToateMasinile(const Repo *repo);

#endif // REPO_H