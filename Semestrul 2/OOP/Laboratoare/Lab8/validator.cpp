//
// Created by Balan Andrei Daniel on 06.04.2025.
//

#include "validator.h"
#include <stdexcept>


bool Validator::isValidDenumire(const std::string& denumire) const {
    if (denumire.empty()) {
        throw std::invalid_argument("Denumirea nu poate fi goala!");
    }
    return true;
}

bool Validator::isValidTip(const std::string& tip) {
    if (tip.empty()) {
        throw std::invalid_argument("Tipul nu poate fi gol!");
    }
    return true;
}

bool Validator::isValidDistanta(float distanta) {
    if (distanta <= 0) {
        throw std::invalid_argument("Distanta trebuie sa fie un numar pozitiv!");
    }
    return true;
}

bool Validator::isValidPret(float pret) const {
    if (pret <= 0) {
        throw std::invalid_argument("Pretul trebuie sa fie un numar pozitiv!");
    }
    return true;
}

bool Validator::isrepetata(const std::string& denumire, const std::string& tip, float distanta, float pret) {
    for (const auto& oferta : repository.getAllOferte()) {
        if (oferta.getDenumire() == denumire && oferta.getTip() == tip && oferta.getDistanta() == distanta && oferta.getPret() == pret) {
            return true;
        }
    }
    return false;
}

bool Validator::isExista(const std::string& denumire) {
    for (const auto& oferta : repository.getAllOferte()) {
        if (oferta.getDenumire() == denumire ) {
            return true;
        }
    }
    return false;
}
Validator::~Validator() = default;



