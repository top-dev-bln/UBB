//
// Created by Balan Andrei Daniel on 17.04.2025.
//

#ifndef WISHLIST_H
#define WISHLIST_H

#include "oferta.h"
#include <vector>


class Wishlist {
private:
    std::vector<Oferta> cos;

public:

    void goleste();

    void adauga(const Oferta& oferta);


    [[nodiscard]] const std::vector<Oferta>& getToate() const;

    void exportCSV(const std::string& numeFisier) const;
    void importCSV(const std::string& numeFisier);


};

#endif //WISHLIST_H