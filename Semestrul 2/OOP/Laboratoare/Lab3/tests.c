#include "service.h"
#include "masina.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void setupMockRepo(Repo *repo) {
    initRepo(repo);
    adaugaMasinaService(repo, "B123ABC", "Dacia", "SUV");
    adaugaMasinaService(repo, "CS13LOL", "BMW", "Sport");
    adaugaMasinaService(repo, "AR16DEF", "Audi", "Sedan");
    adaugaMasinaService(repo, "TM99XYZ", "Mercedes", "SUV");
    adaugaMasinaService(repo, "GL20FRT", "Volkswagen", "Hatchback");
}
void test_adaugaMasinaService() {
    Repo repo;
    initRepo(&repo);

    assert(adaugaMasinaService(&repo, "B123ABD", "Dacia", "SUV") == 1);
    assert(adaugaMasinaService(&repo, "CS13LOL2", "BMW", "Sport") == 1);
    assert(adaugaMasinaService(&repo, "AR16DEG", "Audi", "Sedan") == 1);
    assert(adaugaMasinaService(&repo, "TM99XYA", "Mercedes", "SUV") == 1);
    assert(adaugaMasinaService(&repo, "GL20FRT2", "Volkswagen", "Hatchback") == 1);

    assert(repo.dim == 5);

    assert(adaugaMasinaService(&repo, "B123ABD", "Renault", "Sedan") == 0);
    assert(repo.dim == 5);

    assert(adaugaMasinaService(&repo, "B123ABE", "Dacia", "SUV") == 1);
    assert(adaugaMasinaService(&repo, "CS13LOL3", "BMW", "Sport") == 1);
    assert(adaugaMasinaService(&repo, "AR16DEH", "Audi", "Sedan") == 1);
    assert(adaugaMasinaService(&repo, "TM99XYB", "Mercedes", "SUV") == 1);
    assert(adaugaMasinaService(&repo, "GL20FRT3", "Volkswagen", "Hatchback") == 1);

    assert(repo.dim == 10);

    assert(strcmp(repo.masini[0].nr_inmatriculare, "B123ABD") == 0);
    assert(strcmp(repo.masini[0].model, "Dacia") == 0);
    assert(strcmp(repo.masini[0].categorie, "SUV") == 0);

    assert(strcmp(repo.masini[4].nr_inmatriculare, "GL20FRT2") == 0);
    assert(strcmp(repo.masini[4].model, "Volkswagen") == 0);
    assert(strcmp(repo.masini[4].categorie, "Hatchback") == 0);

    assert(adaugaMasinaService(&repo, "B123ABC", "Dacia", "SUV") == 1);
    assert(repo.dim == 11);

    assert(strcmp(repo.masini[10].nr_inmatriculare, "B123ABC") == 0);
    assert(strcmp(repo.masini[10].model, "Dacia") == 0);
    assert(strcmp(repo.masini[10].categorie, "SUV") == 0);

    assert(adaugaMasinaService(&repo, "B123ABC", "Renault", "Sedan") == 0);
    assert(repo.dim == 11);

    elibereazaRepo(&repo);
}


void test_inchiriereMasinaService() {
    Repo repo;
    setupMockRepo(&repo);


    int index = cautaMasinaDupaInmatriculare(&repo, "B123ABC");
    assert(index != -1);
    inchiriereMasinaService(&repo, "B123ABC");
    assert(repo.masini[index].inchiriata == 1);


    inchiriereMasinaService(&repo, "B123ABC");
    assert(repo.masini[index].inchiriata == 0);


    inchiriereMasinaService(&repo, "XXXXXXX");
    elibereazaRepo(&repo);
}
void test_filtrare() {
    Repo repo;
    setupMockRepo(&repo);

    Masina *filtered = (Masina*)malloc(repo.dim * sizeof(Masina));
    int count;

    count = filtrare(&repo, '1', "SUV", filtered);
    assert(count == 2);
    assert(strcmp(filtered[0].nr_inmatriculare, "B123ABC") == 0);
    assert(strcmp(filtered[1].nr_inmatriculare, "TM99XYZ") == 0);


    count = filtrare(&repo, '2', "BMW", filtered);
    assert(count == 1);
    assert(strcmp(filtered[0].nr_inmatriculare, "CS13LOL") == 0);


    count = filtrare(&repo, '1', "Limuzina", filtered);
    assert(count == 0);

    free(filtered);
    elibereazaRepo(&repo);
}
void test_actualizareMasina() {
    Repo repo;
    initRepo(&repo);

    assert(actualizareMasinaService(&repo, "B123ABC", "Dacia Logan", "Sedan") == 0);

    adaugaMasinaService(&repo, "B123ABC", "Dacia", "SUV");
    adaugaMasinaService(&repo, "CS13LOL", "BMW", "Sport");

    int index = cautaMasinaDupaInmatriculare(&repo, "B123ABC");
    assert(index != -1);
    assert(actualizareMasinaService(&repo, "B123ABC", "Dacia Logan", "Sedan") == 1);
    assert(strcmp(repo.masini[index].model, "Dacia Logan") == 0);
    assert(strcmp(repo.masini[index].categorie, "Sedan") == 0);
    assert(strcmp(repo.masini[index].nr_inmatriculare, "B123ABC") == 0);

    assert(actualizareMasinaService(&repo, "ZZ999ZZ", "Dacia", "SUV") == 0);

    assert(actualizareMasinaService(&repo, "B123ABC", "", "Sedan") == 0);
    assert(actualizareMasinaService(&repo, "B123ABC", "Dacia Logan", "") == 0);

    assert(repo.dim == 2);
    assert(strcmp(repo.masini[index].nr_inmatriculare, "B123ABC") == 0);
    assert(strcmp(repo.masini[index].model, "Dacia Logan") == 0);
    assert(strcmp(repo.masini[index].categorie, "Sedan") == 0);

    elibereazaRepo(&repo);
}
void test_sortareMasini() {
    Repo repo;
    initRepo(&repo);

    assert(adaugaMasinaService(&repo, "B123ABC", "Dacia", "Suv") == 1);
    assert(adaugaMasinaService(&repo, "CS13LOL", "BMW", "Sport") == 1);
    assert(adaugaMasinaService(&repo, "AR16DEF", "Audi", "Sedan") == 1);

    Masina *sorted = (Masina*)malloc(repo.dim * sizeof(Masina));

    int count = sortareMasini(&repo, '1', '1', sorted);
    assert(count == 3);
    assert(strcmp(sorted[0].model, "Audi") == 0);
    assert(strcmp(sorted[1].model, "BMW") == 0);
    assert(strcmp(sorted[2].model, "Dacia") == 0);

    count = sortareMasini(&repo, '1', '2', sorted);
    assert(count == 3);
    assert(strcmp(sorted[0].model, "Dacia") == 0);
    assert(strcmp(sorted[1].model, "BMW") == 0);
    assert(strcmp(sorted[2].model, "Audi") == 0);

    count = sortareMasini(&repo, '2', '1', sorted);
    assert(count == 3);
    assert(strcmp(sorted[0].categorie, "Sedan") == 0);
    assert(strcmp(sorted[1].categorie, "Sport") == 0);
    assert(strcmp(sorted[2].categorie, "Suv") == 0);

    count = sortareMasini(&repo, '2', '2', sorted);
    assert(count == 3);
    assert(strcmp(sorted[0].categorie, "Suv") == 0);
    assert(strcmp(sorted[1].categorie, "Sport") == 0);
    assert(strcmp(sorted[2].categorie, "Sedan") == 0);

    assert(adaugaMasinaService(&repo, "X123ABC", "Ford", "Convertible") == 1);
    assert(adaugaMasinaService(&repo, "Y456DEF", "Chevrolet", "Sedan") == 1);

    count = sortareMasini(&repo, '2', '1', sorted);

    assert(count == 5);
    assert(strcmp(sorted[0].categorie, "Convertible") == 0);
    assert(strcmp(sorted[1].categorie, "Sedan") == 0);
    assert(strcmp(sorted[2].categorie, "Sedan") == 0);
    assert(strcmp(sorted[3].categorie, "Sport") == 0);
    assert(strcmp(sorted[4].categorie, "Suv") == 0);

    count = sortareMasini(&repo, '2', '2', sorted);
    assert(count == 5);
    assert(strcmp(sorted[0].categorie, "Suv") == 0);
    assert(strcmp(sorted[1].categorie, "Sport") == 0);
    assert(strcmp(sorted[2].categorie, "Sedan") == 0);
    assert(strcmp(sorted[3].categorie, "Sedan") == 0);
    assert(strcmp(sorted[4].categorie, "Convertible") == 0);


    free(sorted);
    elibereazaRepo(&repo);
}

void run_all_tests() {
    test_adaugaMasinaService();
    test_actualizareMasina();
    test_inchiriereMasinaService();
    test_filtrare();
    test_sortareMasini();
    printf("Toate testele pentru service au trecut cu succes!\n");
}

