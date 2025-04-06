//
// Created by Balan Andrei Daniel on 03.04.2025.
//

#include "oferta.h"
#include "repository.h"
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
    Service service;

    service.addOferta("Palma de Mallorca", "plaja", 2.5, 100000);
    service.addOferta("Barcelona", "oras", 3.0, 50000);

    auto all = service.getAllOferte();
    assert(all.size() == 2);

    service.modifyOferta("Palma de Mallorca", "insula", 2.8, 120000);
    auto modified = service.searchOferta("Palma de Mallorca");
    assert(modified.getTip() == "insula");
    assert(modified.getDistanta() == 2.8f);
    assert(modified.getPret() == 120000);

    service.deleteOferta("Barcelona");
    all = service.getAllOferte();
    assert(all.size() == 1);
    assert(all[0].getDenumire() == "Palma de Mallorca");

    service.addOferta("Madrid", "oras", 4.0, 60000);
    auto filteredByPret = service.filterByPret(100000);
    assert(filteredByPret.size() == 1);

    auto filteredByDestinatie = service.filterByDestinatie("Madrid");
    assert(filteredByDestinatie.size() == 1);
    assert(filteredByDestinatie[0].getDenumire() == "Madrid");

    auto sortedByDenumire = service.sortByDenumire();
    assert(sortedByDenumire[0].getDenumire() == "Madrid");

    auto sortedByDestinatie = service.sortByDestinatie();
    assert(sortedByDestinatie[0].getTip() == "insula");

    service.addOferta("Undeva fain", "plaja", 4.0, 432);
    service.addOferta("Undeva fain2", "plaja", 4.0, 432);
    service.addOferta("Undeva nasol", "balamuc", 4.0, 432);
    auto sortedByTipAndPret = service.sortByTipAndPret();
    assert(sortedByTipAndPret[0].getDenumire() == "Undeva nasol");
}

void testall() {
    test_oferta();
    test_repository();
    test_service();
}