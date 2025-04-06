#pragma once

typedef struct {
    int id;
    char* tip;
    int suprafata;
    char* adresa;
    int pret;
} Oferta;

// Creează o ofertă cu alocare dinamică
Oferta* createOferta(int id, const char* tip,int  suprafata, const char* adresa, int pret);

// Distruge oferta și eliberează memoria dinamică
void destroyOferta(Oferta* o);

// Validare pentru formatul adresei
int esteAdresaValida(const char* data);

// Funcție pentru validarea unei oferte
int valideazaOferta(Oferta* o);

// Funcție pentru copierea unei oferte
void* copyOferta(void* o);
