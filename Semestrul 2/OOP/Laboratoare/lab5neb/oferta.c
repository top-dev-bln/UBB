#include "oferta.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// Creează o ofertă (cu alocare dinamică pentru câmpuri)
Oferta* createOferta(int id, const char* tip, int suprafata, const char* adresa, int pret) {
	/* Creează o ofertă nouă cu alocare dinamică pentru câmpuri.
	 * Parametri:
	 * id - identificatorul unic al ofertei (int).
	 * tip - tipul ofertei (char*).
	 * suprafata - suprafata ofertei (int).
	 * adresa - adresa ofertei (char*).
	 * pret - prețul ofertei (int).
     */
    Oferta* o = (Oferta*)malloc(sizeof(Oferta));

    o->id = id;
    o->pret = pret;
    o->suprafata = suprafata;

    size_t tip_len = strlen(tip) + 1;
    size_t adr_len = strlen(adresa) + 1;

    o->tip = (char*)malloc(tip_len);
    o->adresa = (char*)malloc(adr_len);

    // Copiem datele în câmpurile alocate
    strcpy(o->tip, tip);
    strcpy(o->adresa, adresa);

    return o;
}

void destroyOferta(Oferta* o) {
    /*Distruge oferta și eliberează memoria dinamică alocată
	 * Parametri:
	 * o - pointer la Oferta
	 */
	if (o != NULL) {
        free(o->tip);
        free(o->adresa);
        free(o);
    }
}

int esteAdresaValida(const char* address) {
    int len = (int)strlen(address);
    if (len < 5) return 0;

    int i = 0;
    while (i < len && isalpha(address[i])) i++; 

    if (i == 0 || address[i] != ',') return 0;
    i++;

    if (strncmp(&address[i], "nr.", 3) != 0) return 0; 
    i += 3;

    if (!isdigit(address[i])) return 0;

    while (i < len && isdigit(address[i])) i++; 

    return i == len;
}


int valideazaOferta(Oferta* o) {
	/* Validează o ofertă
	 * Parametri:
	 * o - pointer la Oferta
	 * Returnează:
	 * 1 dacă oferta este validă
	 * 2 dacă tipul ofertei nu este valid
	 * 3 dacă suprafata este negativa
	 * 4 dacă adresa nu este validă
	 * 5 dacă prețul este negativ
 	 */
    if (strcmp(o->tip, "casa") != 0 && strcmp(o->tip, "apartament") != 0 && strcmp(o->tip, "teren") != 0) {
        return 2; 
    }

    if (o->suprafata <= 0) {
        return 3;
    }

    if (!esteAdresaValida(o->adresa)) {
        return 4; 
    }

    if (o->pret <= 0) {
        return 5; 
    }

    return 1; 
}

void* copyOferta(void* o)
{
	/* Copiază o ofertă
	 * Parametri:
	 * o - pointer la Oferta
	 * Returnează:
	 * pointer la o nouă ofertă
	 */
	Oferta* ofertaOriginala = (Oferta*)o;
	return createOferta(ofertaOriginala->id, ofertaOriginala->tip, ofertaOriginala->suprafata, ofertaOriginala->adresa, ofertaOriginala->pret);

}