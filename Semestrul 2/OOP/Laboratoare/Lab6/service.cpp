//
// Created by Balan Andrei Daniel on 03.04.2025.
//

#include "service.h"


void Service::addOferta(const std::string& denumire, const std::string& tip, float distanta, float pret) {
    repo.addOferta(Oferta(denumire, tip, distanta, pret));
}

void Service::modifyOferta(const std::string& denumire, const std::string& tip, float distanta, float pret) {
    repo.modifyOferta(denumire, tip, distanta, pret);
}

void Service::deleteOferta(const std::string& denumire) {
    repo.deleteOferta(denumire);
}

[[nodiscard]] std::vector<Oferta> Service::getAllOferte() const {
    return repo.getAllOferte();
}

[[nodiscard]] std::vector<Oferta> Service::filterByDestinatie(const std::string& destinatie) const {
    std::vector<Oferta> result;
    const std::vector<Oferta>& oferte = repo.getAllOferte();

    for (const Oferta& oferta : oferte) {
        if (oferta.getDenumire() == destinatie) {
            result.push_back(oferta);
        }
    }
    return result;
}




[[nodiscard]] std::vector<Oferta> Service::filterByPret(float pret) const {
    std::vector<Oferta> result;
    const std::vector<Oferta>& oferte = repo.getAllOferte();
    for (const Oferta& oferta : oferte) {
        if (oferta.getPret() <= pret) {
            result.push_back(oferta);
        }
    }
    return result;
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
    return repo.searchOferta(denumire);
}

