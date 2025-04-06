//
// Created by Balan Andrei Daniel on 03.04.2025.
//

#ifndef SERVICE_H
#define SERVICE_H

#include <string>
#include <vector>
#include "oferta.h"
#include "repository.h"

class Service {
private:
    Repository repo;

public:
    void addOferta(const std::string& denumire, const std::string& tip, float distanta, float pret);
    void modifyOferta(const std::string& denumire, const std::string& tip, float distanta, float pret);
    void deleteOferta(const std::string& denumire);
    [[nodiscard]] std::vector<Oferta> getAllOferte() const;
    [[nodiscard]] std::vector<Oferta> filterByDestinatie(const std::string& destinatie) const;
    [[nodiscard]] std::vector<Oferta> filterByPret(float pret) const;
    [[nodiscard]] std::vector<Oferta> sortByDenumire() const;
    [[nodiscard]] std::vector<Oferta> sortByDestinatie() const;
    [[nodiscard]] std::vector<Oferta> sortByTipAndPret() const;
    [[nodiscard]] Oferta searchOferta(const std::string& denumire) const;
};

#endif //SERVICE_H
