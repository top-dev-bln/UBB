//
// Created by Balan Andrei Daniel on 03.04.2025.
//

#ifndef SERVICE_H
#define SERVICE_H

#include <string>
#include <vector>
#include "oferta.h"
#include "repository.h"
#include "validator.h"

class Service {
private:
    Repository& repo;
    Validator& validator;

public:
    Service(Repository& repo, Validator& validator) : repo(repo), validator(validator) {}
    void addOferta(const std::string& denumire, const std::string& tip, float distanta, float pret);
    void modifyOferta(const std::string& denumire, const std::string& tip, float distanta, float pret);
    void deleteOferta(const std::string& denumire);

    [[nodiscard]] IteratorVector<Oferta> begin() const ;
    [[nodiscard]] IteratorVector<Oferta> end() const ;

    [[nodiscard]] VectorDinamic<Oferta> filterByDestinatie(const std::string& destinatie) const;
    [[nodiscard]] VectorDinamic<Oferta> filterByPret(float pret) const;
    [[nodiscard]] VectorDinamic<Oferta> sortByDenumire() const;
    [[nodiscard]] VectorDinamic<Oferta> sortByDestinatie() const;
    [[nodiscard]] VectorDinamic<Oferta> sortByTipAndPret() const;
    [[nodiscard]] Oferta searchOferta(const std::string& denumire) const;
};

#endif //SERVICE_H
