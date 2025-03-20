//
// Created by Balan Andrei Daniel on 13.03.2025.
//

#ifndef SERVICE_H
#define SERVICE_H

#include "repo.h"

int actualizareMasinaService(Repo *repo, const char *nr_inmatriculare, const char *model_nou, const char *categorie_noua);
int adaugaMasinaService(Repo *repo, const char *nr_inmatriculare, const char *model, const char *categorie);
void inchiriereMasinaService(Repo *repo, const char *nr_inmatriculare);
int filtrare(Repo *repo, char subOpt, const char *filtru, Masina *filtered);
int sortareMasini(Repo *repo, char criteriu, char ordine, Masina *sorted);
#endif // SERVICE_H