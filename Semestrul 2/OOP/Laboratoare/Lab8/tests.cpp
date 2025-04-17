//
// Created by Balan Andrei Daniel on 03.04.2025.
//

#include "oferta.h"
#include "repository.h"
#include "wishlist.h"
#include "service.h"
#include <cassert>

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

    auto all = repo.getAllOferte();
    assert(all.size() == 2);

    repo.modifyOferta("Palma de Mallorca", "insula", 2.8, 120000);
    auto modified = repo.searchOferta("Palma de Mallorca");
    assert(modified.getTip() == "insula");
    assert(modified.getDistanta() == 2.8f);
    assert(modified.getPret() == 120000);

    repo.deleteOferta("Barcelona");
    all = repo.getAllOferte();
    assert(all.size() == 1);
    assert(all[0].getDenumire() == "Palma de Mallorca");
}

void test_service() {
    Repository repo_test;
    Validator validator_test(repo_test);
    Wishlist wishlist_test;
    Service servic_test(repo_test, validator_test, wishlist_test);

    servic_test.addOferta("Palma de Mallorca", "plaja", 2.5, 100000);
    servic_test.addOferta("Barcelona", "oras", 3.0, 50000);

    auto all = servic_test.getAllOferte();
    assert(all.size() == 2);

    servic_test.modifyOferta("Palma de Mallorca", "insula", 2.8, 120000);
    auto modified = servic_test.searchOferta("Palma de Mallorca");
    assert(modified.getTip() == "insula");
    assert(modified.getDistanta() == 2.8f);
    assert(modified.getPret() == 120000);

    servic_test.deleteOferta("Barcelona");
    all = servic_test.getAllOferte();
    assert(all.size() == 1);
    assert(all[0].getDenumire() == "Palma de Mallorca");

    servic_test.addOferta("Madrid", "oras", 4.0, 60000);
    auto filteredByPret = servic_test.filterByPret(100000);
    assert(filteredByPret.size() == 1);

    auto filteredByDestinatie = servic_test.filterByDestinatie("Madrid");
    assert(filteredByDestinatie.size() == 1);
    assert(filteredByDestinatie[0].getDenumire() == "Madrid");

    auto sortedByDenumire = servic_test.sortByDenumire();
    assert(sortedByDenumire[0].getDenumire() == "Madrid");

    auto sortedByDestinatie = servic_test.sortByDestinatie();
    assert(sortedByDestinatie[0].getTip() == "insula");

    servic_test.addOferta("Madrid", "ceva fain", 4.0, 60000);

    servic_test.addOferta("Madrid", "ceva fain", 4.0, 50000);
    auto sortedByTipAndPret = servic_test.sortByTipAndPret();
    assert(sortedByTipAndPret[0].getDenumire() == "Madrid");
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

void test_wishlist() {
    Wishlist wishlist;
    Repository repo_test;
    Validator validator_test(repo_test);
    Service servic_test(repo_test, validator_test, wishlist);

    servic_test.addOferta("Palma de Mallorca", "plaja", 2.5, 100000);
    servic_test.addOferta("Barcelona", "oras", 3.0, 50000);
    servic_test.addOferta("Madrid", "oras", 4.0, 60000);
    servic_test.addOferta("Bucuresti", "oras", 1.0, 20000);
    servic_test.addOferta("Cluj", "oras", 2.0, 30000);




    try {
        servic_test.genereazaWishlist(-1);
        assert(false);
    } catch (const std::invalid_argument&) {
        assert(true);
    }

    try{
        servic_test.genereazaWishlist(100);
        assert(false);
    } catch (const std::runtime_error&) {
        assert(true);
    }




    servic_test.genereazaWishlist(3);
    auto allWishlist = servic_test.getAllWishlist();
    assert(allWishlist.size() == 3);



    try {
        servic_test.adaugaInWishlist("inexistent");
        assert(false);
    } catch (const std::runtime_error&) {
        assert(true);
    }


    servic_test.exportCSV("fisier.csv");
    servic_test.golesteWishlist();


    assert(servic_test.getAllWishlist().size() == 0);
    servic_test.importCSV("fisier.csv");

    assert(servic_test.getAllWishlist().size() == 3);




}


void testall() {
    test_oferta();
    test_repository();
    test_service();
    test_validator();
    test_wishlist();
}

