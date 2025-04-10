#ifndef REPOSITORY_H
#define REPOSITORY_H

#include <vector>
#include "VectorDinamic.h"
#include "oferta.h"

class Repository {
private:
    VectorDinamic<Oferta> oferte;

public:
    void addOferta(const Oferta& oferta);
    void modifyOferta(const std::string& denumire, const std::string& tip, float distanta, float pret) const;
    void deleteOferta(const std::string& denumire);
    [[nodiscard]] IteratorVector<Oferta> begin() const;
    [[nodiscard]] IteratorVector<Oferta> end() const;

    [[nodiscard]] Oferta searchOferta(const std::string& denumire) const;
};

#endif // REPOSITORY_H
