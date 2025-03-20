//
// Created by Balan Andrei Daniel on 13.03.2025.
//

#ifndef MASINA_H
#define MASINA_H

#define MAX_LEN 50

typedef struct {
    char nr_inmatriculare[MAX_LEN];
    char model[MAX_LEN];
    char categorie[MAX_LEN];
    int inchiriata;
} Masina;

void creareMasina(Masina *m, const char *nr_inmatriculare, const char *model, const char *categorie);
void afisareMasina(const Masina *m);

#endif