//
// Created by Balan Andrei Daniel on 03.04.2025.
//
#ifndef OFERTA_H
#define OFERTA_H

#include <string>

class Oferta {
private:
    std::string denumire;
    std::string tip;
    float distanta;
    float pret;

public:

    Oferta(std::string denumire, std::string tip, float distanta,float pret);


    [[nodiscard]] std::string getDenumire() const;
    [[nodiscard]] std::string getTip() const;
    [[nodiscard]] float getDistanta() const;
    [[nodiscard]] float getPret() const;


    void setDenumire(const std::string &denumire);
    void setTip(const std::string &tip);
    void setDistanta(float distanta);
    void setPret(float pret);


    ~Oferta();
};

#endif // OFERTA_H