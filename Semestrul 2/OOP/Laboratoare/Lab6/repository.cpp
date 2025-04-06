#include "repository.h"
#include <algorithm>


void Repository::addOferta(const Oferta& oferta) {
    oferte.push_back(oferta);
}

void Repository::modifyOferta(const std::string& denumire, const std::string& tip, float distanta, float pret) {
    for (auto& oferta : oferte) {
        if (oferta.getDenumire() == denumire) {
            oferta.setTip(tip);
            oferta.setDistanta(distanta);
            oferta.setPret(pret);
            return;
        }
    }

}

void Repository::deleteOferta(const std::string& denumire) {
    auto it = std::remove_if(oferte.begin(), oferte.end(), [&](const Oferta& oferta) {
        return oferta.getDenumire() == denumire;
    });

    oferte.erase(it, oferte.end());
}

const std::vector<Oferta>& Repository::getAllOferte() const {
    return oferte;
}

Oferta Repository::searchOferta(const std::string& denumire) const {
    for (const auto& oferta : oferte) {
        if (oferta.getDenumire() == denumire) {
            return oferta;
        }
    }
    throw std::runtime_error("Oferta not found");

}
