//
// Created by Balan Andrei Daniel on 03.04.2025.
//

#include "service.h"
#include <algorithm>
#include <random>
#include <chrono>

void Service::adaugaInWishlist(const std::string& denumire) {
    if (validator.isValidDenumire(denumire) && validator.isExista(denumire)) {
        auto oferta = searchOferta(denumire);

        wishlist.adauga(oferta);
    }
    else {
        throw std::runtime_error("Oferta nu exista!");
    }

}

void Service::golesteWishlist() {
    wishlist.goleste();
}

void Service::genereazaWishlist(int numar) {
    if (numar <= 0) {
        throw std::invalid_argument("Numarul de oferte trebuie sa fie pozitiv!");
    }

    std::vector<Oferta> oferte = repo.getAllOferte();

    if (numar > oferte.size()) {
        throw std::runtime_error("Nu exista suficiente oferte pentru a genera wishlist-ul!");
    }


    auto seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::shuffle(oferte.begin(), oferte.end(), std::default_random_engine(seed));



    for (int i = 0; i < numar; ++i) {

        adaugaInWishlist(oferte[i].getDenumire());


    }
}

void Service::exportCSV(const std::string& numeFisier) const {
    wishlist.exportCSV(numeFisier);
}

void Service::importCSV(const std::string& numeFisier) {
    wishlist.importCSV(numeFisier);
}

[[nodiscard]] std::vector<Oferta> Service::getAllWishlist() const {
    return wishlist.getToate();
}




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

[[nodiscard]] std::vector<Oferta> Service::getAllOferte() const {
    return repo.getAllOferte();
}

[[nodiscard]] std::vector<Oferta> Service::filterByDestinatie(const std::string& destinatie) const {
    std::vector<Oferta> result;
    const std::vector<Oferta>& oferte = repo.getAllOferte();

    std::copy_if(oferte.begin(), oferte.end(), std::back_inserter(result),
        [&destinatie](const Oferta& oferta) {
            return oferta.getDenumire() == destinatie;
        });

    return result;
}




[[nodiscard]] std::vector<Oferta> Service::filterByPret(float pret) const {
    if (validator.isValidPret(pret)) {
        std::vector<Oferta> result;
        const std::vector<Oferta>& oferte = repo.getAllOferte();
        std::copy_if(oferte.begin(), oferte.end(), std::back_inserter(result),
            [pret](const Oferta& oferta) {
                return oferta.getPret() <= pret;
            });
        return result;
    }


}


[[nodiscard]] std::vector<Oferta> Service::sortByDenumire() const {
    auto sorted = repo.getAllOferte();
    std::sort(sorted.begin(), sorted.end(), [](const Oferta& a, const Oferta& b) {
        return a.getDenumire() < b.getDenumire();
    });
    return sorted;
}

[[nodiscard]] std::vector<Oferta> Service::sortByDestinatie() const {
    auto sorted = repo.getAllOferte();
    std::sort(sorted.begin(), sorted.end(), [](const Oferta& a, const Oferta& b) {
        return a.getTip() < b.getTip();
    });
    return sorted;
}

[[nodiscard]] std::vector<Oferta> Service::sortByTipAndPret() const {
    auto sorted = repo.getAllOferte();
    std::sort(sorted.begin(), sorted.end(), [](const Oferta& a, const Oferta& b) {
        if (a.getTip() < b.getTip()) {
            return true;
        }
        if (a.getTip() > b.getTip()) {
            return false;
        }
        return a.getPret() < b.getPret();
    });
    return sorted;
}

[[nodiscard]] Oferta Service::searchOferta(const std::string& denumire) const {
    if (validator.isValidDenumire(denumire)) {
        return repo.searchOferta(denumire);
    }

}

