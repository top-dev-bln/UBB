//
// Created by Balan Andrei Daniel on 13.03.2025.
//
#include "masina.h"
#include <stdio.h>
#include <string.h>

void creareMasina(Masina *m, const char *nr_inmatriculare, const char *model, const char *categorie) {
    // input : m - pointer la masina , nr_inmatriculare - pointer la sir de caractere, model - pointer la sir de caractere, categorie - pointer la sir de caractere
    // output : - , functia initializeaza un obiect de tip Masina cu datele primite ca parametrii
    strncpy(m->nr_inmatriculare, nr_inmatriculare, MAX_LEN - 1);
    m->nr_inmatriculare[MAX_LEN - 1] = '\0';
    strncpy(m->model, model, MAX_LEN - 1);
    m->model[MAX_LEN - 1] = '\0';
    strncpy(m->categorie, categorie, MAX_LEN - 1);
    m->categorie[MAX_LEN - 1] = '\0';
    m->inchiriata = 0;
}

