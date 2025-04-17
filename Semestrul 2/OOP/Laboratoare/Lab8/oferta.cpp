//
// Created by Balan Andrei Daniel on 03.04.2025.
//

#include "oferta.h"
#include <iostream>







    Oferta::Oferta(std::string denumire, std::string tip, float distanta, float pret)
        : denumire(denumire), tip(tip), distanta(distanta), pret(pret) {}

    [[nodiscard]] std::string Oferta::getDenumire() const {
        return denumire;
    }
    [[nodiscard]] std::string Oferta::getTip() const {
        return tip;
    }
    [[nodiscard]] float Oferta::getDistanta() const {
        return distanta;
    }
    [[nodiscard]] float Oferta::getPret() const {
        return pret;
    }


    void Oferta::setDenumire(const std::string &denumire) {
        this->denumire = denumire;
    }
    void Oferta::setTip(const std::string &tip) {
        this->tip = tip;
    }
    void Oferta::setDistanta(const float distanta) {
        this->distanta = distanta;
    }
    void Oferta::setPret(const float pret) {
        this->pret = pret;
    }


    Oferta::~Oferta() = default;




