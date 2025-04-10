#include "repository.h"
#include "oferta.h"


void Repository::addOferta(const Oferta& oferta) {
    oferte.push_back(oferta);
}

void Repository::modifyOferta(const std::string& denumire, const std::string& tip, float distanta, float pret) const {
    for (auto it = oferte.begin(); it.valid(); it.next()) {
        if (it.element().getDenumire() == denumire) {
            it.element().setTip(tip);
            it.element().setDistanta(distanta);
            it.element().setPret(pret);
            return;
        }
    }
}

void Repository::deleteOferta(const std::string& denumire) {
    for (auto it = oferte.begin(); it.valid(); it.next()) {
        if (it.element().getDenumire() == denumire) {

            oferte.erase(it);

            return;
        }
    }
}

IteratorVector<Oferta> Repository::begin() const {
    return oferte.begin();
}




Oferta Repository::searchOferta(const std::string& denumire) const {
    for (auto it = oferte.begin(); it.valid(); it.next()) {
        if (it.element().getDenumire() == denumire) {
            return it.element();
        }
    }
    throw std::out_of_range("Nu exista oferta cu aceasta denumire!");
}