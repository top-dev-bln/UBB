//
// Created by Balan Andrei Daniel on 03.04.2025.
//

#include "oferta.h"
#include "repository.h"
#include "service.h"
#include <cassert>
#include <iostream>

void test_oferta() {
    Oferta of1("Palma de Mallorca", "plaja", 2.5, 100000);
    assert(of1.getDenumire() == "Palma de Mallorca");
    assert(of1.getTip() == "plaja");
    assert(of1.getDistanta() == 2.5f);
    assert(of1.getPret() == 100000);

    of1.setDenumire("Barcelona");
    of1.setTip("oras");
    of1.setDistanta(3.0f);
    of1.setPret(50000);
    assert(of1.getDenumire() == "Barcelona");
    assert(of1.getTip() == "oras");
    assert(of1.getDistanta() == 3.0f);
    assert(of1.getPret() == 50000);
}

void test_repository() {
    Repository repo;
    repo.addOferta(Oferta("Palma de Mallorca", "plaja", 2.5, 100000));
    repo.addOferta(Oferta("Barcelona", "oras", 3.0, 50000));


    auto it = repo.begin();


    assert(it.valid());
    assert(it.element().getDenumire() == "Palma de Mallorca");
    it.next();
    assert(it.valid());
    assert(it.element().getDenumire() == "Barcelona");
    it.next();
    assert(!it.valid());



    repo.modifyOferta("Palma de Mallorca", "insula", 2.8, 120000);
    auto modified = repo.searchOferta("Palma de Mallorca");
    assert(modified.getTip() == "insula");
    assert(modified.getDistanta() == 2.8f);
    assert(modified.getPret() == 120000);

    repo.deleteOferta("Barcelona");


    auto it4 = repo.begin();
    assert(it4.valid());
    assert(it4.element().getDenumire() == "Palma de Mallorca");
    it4.next();
    assert(!it4.valid());

    repo.deleteOferta("Barcelona");


        try {
            repo.searchOferta("OfertaInexistenta");
            assert(false);
        } catch (const std::out_of_range& e) {
            assert(true);
        }
    }



void test_service() {
    Repository repo_test;
    Validator validator_test(repo_test);
    Service servic_test(repo_test, validator_test);



    servic_test.addOferta("Palma de Mallorca", "plaja", 2.5, 100000);
    servic_test.addOferta("Barcelona", "oras", 3.0, 50000);

    auto it = servic_test.begin();
    assert(it.valid());
    assert(it.element().getDenumire() == "Palma de Mallorca");
    it.next();
    assert(it.valid());
    assert(it.element().getDenumire() == "Barcelona");
    it.next();
    assert(!it.valid());

    auto it2 = servic_test.begin();
    assert(it2.valid());
    assert(it2.element().getDenumire() == "Palma de Mallorca");

    servic_test.modifyOferta("Palma de Mallorca", "insula", 2.8, 120000);
    auto modified = servic_test.searchOferta("Palma de Mallorca");
    assert(modified.getTip() == "insula");
    assert(modified.getDistanta() == 2.8f);
    assert(modified.getPret() == 120000);

    servic_test.deleteOferta("Barcelona");

    auto it3 = servic_test.begin();
    int count = 0;
    while (it3.valid()) {
        count++;
        it3.next();
    }
    assert(count == 1);  // Ar trebui să fie doar o ofertă
    auto it4 = servic_test.begin();
    assert(it4.valid());
    assert(it4.element().getDenumire() == "Palma de Mallorca");

    servic_test.addOferta("Madrid", "oras", 4.0, 60000);
    auto filteredByPret = servic_test.filterByPret(100000);
    assert(filteredByPret.size() == 1);

    auto filteredByDestinatie = servic_test.filterByDestinatie("Madrid");
    auto itfiltrare = filteredByDestinatie.begin();
    assert(itfiltrare.valid());
    assert(itfiltrare.element().getDenumire() == "Madrid");

    servic_test.addOferta("a","a",1,1);

    auto sortedByDenumire = servic_test.sortByDenumire();
    auto itsortDen = sortedByDenumire.begin();
    assert(itsortDen.valid());
    assert(itsortDen.element().getDenumire() == "Madrid");

    auto sortedByDestinatie = servic_test.sortByDestinatie();
    auto itsortDest = sortedByDestinatie.begin();
    assert(itsortDest.valid());
    assert(itsortDest.element().getTip() == "a");

    servic_test.addOferta("Madrid", "ceva fain", 4.0, 60000);
    servic_test.addOferta("Madrid", "ceva fain", 4.0, 50000);
    auto sortedByTipAndPret = servic_test.sortByTipAndPret();
    auto itsortTipPret = sortedByTipAndPret.begin();
    assert(itsortTipPret.valid());
    assert(itsortTipPret.element().getDenumire() == "a");

    servic_test.addOferta("b","b",1,1);
    servic_test.deleteOferta("b");
}
void test_validator() {
    Repository repo_test;
    Validator validator_test(repo_test);


    try {
        (void) validator_test.isValidDenumire("");
        assert(false);
    } catch (const std::invalid_argument&) {
        assert(true);
    }
    try {
        (void) validator_test.isValidTip("");
        assert(false);
    } catch (const std::invalid_argument&) {
        assert(true);
    }

    try {
        (void) validator_test.isValidDistanta(-1);
        assert(false);
    } catch (const std::invalid_argument&) {
        assert(true);
    }

    try {
        (void) validator_test.isValidPret(-1);
        assert(false);
    } catch (const std::invalid_argument&) {
        assert(true);
    }

    assert(validator_test.isExista("Palma de Mallorca")==false);
    repo_test.addOferta(Oferta("Palma de Mallorca", "plaja", 2.5, 100000));
    assert(validator_test.isExista("Palma de Mallorca")==true);

    assert(validator_test.isrepetata("Palma de Mallorca", "plaja", 2.5, 100000)==true);

    repo_test.deleteOferta("Palma de Mallorca");
    assert(validator_test.isrepetata("Palma de Mallorca", "plaja", 2.5, 100000)==false);





}


void test_erase_direct() {




    VectorDinamic<Oferta> vec;
    auto it1 = IteratorVector<Oferta>(vec, 0);
    try {
        (void) it1.element();
        assert(false);
    } catch (const std::invalid_argument&) {
        assert(true);
    };

    vec.push_back(Oferta("a", "a", 1, 1));
    vec.push_back(Oferta("b", "b", 2, 2));
    vec.push_back(Oferta("c", "c", 3, 3));

    auto it = vec.begin();  // poz = 0
    vec.erase(it);

    assert(vec.size() == 2);
    assert(vec.get_element(0).getDenumire() == "b");
    assert(vec.get_element(1).getDenumire() == "c");

    try {
        VectorDinamic<int> v;
        v.get_element(0);
        assert(false);
    } catch (const std::out_of_range& e) {
        assert(true);
    }


}


void testall() {
    test_oferta();
    test_repository();
    test_service();
    test_validator();
    test_erase_direct();
}

