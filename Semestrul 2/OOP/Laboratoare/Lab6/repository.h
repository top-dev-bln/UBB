#ifndef REPOSITORY_H
#define REPOSITORY_H

#include <vector>
#include <string>
#include "oferta.h"

class Repository {
private:
    std::vector<Oferta> oferte;

public:
    void addOferta(const Oferta& oferta);
    void modifyOferta(const std::string& denumire, const std::string& tip, float distanta, float pret);
    void deleteOferta(const std::string& denumire);
    [[nodiscard]] const std::vector<Oferta>& getAllOferte() const;
    [[nodiscard]] Oferta searchOferta(const std::string& denumire) const;
};

#endif // REPOSITORY_H
