//
// Created by Balan Andrei Daniel on 03.04.2025.
//

#include "service.h"
#include "VectorDinamic.h"



void Service::addOferta(const std::string& denumire, const std::string& tip, float distanta, float pret) {
    if (validator.isValidDenumire(denumire) && validator.isValidTip(tip) && validator.isValidDistanta(distanta) && validator.isValidPret(pret) && !validator.isrepetata(denumire, tip, distanta, pret)) {
        repo.addOferta(Oferta(denumire, tip, distanta, pret));
    }
}

void Service::modifyOferta(const std::string& denumire, const std::string& tip, float distanta, float pret) {
    if (validator.isValidDenumire(denumire) && validator.isValidTip(tip) && validator.isValidDistanta(distanta) && validator.isValidPret(pret) && validator.isExista(denumire)) {
        repo.modifyOferta(denumire, tip, distanta, pret);
    }

}

void Service::deleteOferta(const std::string& denumire) {
    if (validator.isValidDenumire(denumire) && validator.isExista(denumire)) {
        repo.deleteOferta(denumire);
    }

}

[[nodiscard]] IteratorVector<Oferta> Service::begin() const {
    return repo.begin();
}


[[nodiscard]] VectorDinamic<Oferta> Service::filterByDestinatie(const std::string& destinatie) const {
    VectorDinamic<Oferta> result;

    for (auto it = repo.begin(); it.valid(); it.next()) {
        const Oferta& oferta = it.element();
        if (oferta.getDenumire() == destinatie) {
            result.push_back(oferta);
        }
    }

    return result;
}



[[nodiscard]] VectorDinamic<Oferta> Service::filterByPret(float pret) const {
    VectorDinamic<Oferta> result;
    for (auto it = repo.begin(); it.valid(); it.next()) {
        const Oferta& oferta = it.element();
        if (oferta.getPret() < pret) {
            result.push_back(oferta);
        }
    }
    return result;
}



[[nodiscard]] VectorDinamic<Oferta> Service::sortByDenumire() const {
    VectorDinamic<Oferta> sorted;

    for (auto it = repo.begin(); it.valid(); it.next()) {
        sorted.push_back(it.element());
    }


    for (auto it1 = sorted.begin(); it1.valid(); it1.next()) {
        for (auto it2 = it1; it2.valid(); it2.next()) {
            if (it1.element().getDenumire() > it2.element().getDenumire()) {

                Oferta temp = it1.element();
                it1.element() = it2.element();
                it2.element() = temp;
            }
        }
    }

    return sorted;
}

[[nodiscard]] VectorDinamic<Oferta> Service::sortByDestinatie() const {
    VectorDinamic<Oferta> sorted;

    for (auto it = repo.begin(); it.valid(); it.next()) {
        sorted.push_back(it.element());
    }


    for (auto it1 = sorted.begin(); it1.valid(); it1.next()) {
        for (auto it2 = it1; it2.valid(); it2.next()) {
            if (it1.element().getTip() > it2.element().getTip()) {
                // Swap elements
                Oferta temp = it1.element();
                it1.element() = it2.element();
                it2.element() = temp;
            }
        }
    }

    return sorted;
}

[[nodiscard]] VectorDinamic<Oferta> Service::sortByTipAndPret() const {
    VectorDinamic<Oferta> sorted;

    for (auto it = repo.begin(); it.valid(); it.next()) {
        sorted.push_back(it.element());
    }

    for (auto it1 = sorted.begin(); it1.valid(); it1.next()) {
        for (auto it2 = it1; it2.valid(); it2.next()) {
            if (it1.element().getTip() > it2.element().getTip() ||
                (it1.element().getTip() == it2.element().getTip() && it1.element().getPret() > it2.element().getPret())) {

                Oferta temp = it1.element();
                it1.element() = it2.element();
                it2.element() = temp;
            }
        }
    }

    return sorted;
}

[[nodiscard]] Oferta Service::searchOferta(const std::string& denumire) const {
    if (validator.isValidDenumire(denumire)) {
        return repo.searchOferta(denumire);
    }

    throw std::out_of_range("Oferta cu aceasta denumire nu exista!");

}

