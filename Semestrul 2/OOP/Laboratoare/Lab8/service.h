//
// Created by Balan Andrei Daniel on 03.04.2025.
//

#ifndef SERVICE_H
#define SERVICE_H


#include <vector>
#include "oferta.h"
#include "repository.h"
#include "validator.h"
#include "wishlist.h"

class Service {
private:
    Repository& repo;
    Validator& validator;
    Wishlist& wishlist;

public:
    Service(Repository& repo, Validator& validator, Wishlist& wlist) : repo(repo), validator(validator), wishlist(wlist) {}
    void addOferta(const std::string& denumire, const std::string& tip, float distanta, float pret);
    void modifyOferta(const std::string& denumire, const std::string& tip, float distanta, float pret);
    void deleteOferta(const std::string& denumire);
    [[nodiscard]] std::vector<Oferta> getAllOferte() const;
    [[nodiscard]] std::vector<Oferta> filterByDestinatie(const std::string& destinatie) const;
    [[nodiscard]] std::vector<Oferta> filterByPret(float pret) const;
    [[nodiscard]] std::vector<Oferta> sortByDenumire() const;
    [[nodiscard]] std::vector<Oferta> sortByDestinatie() const;
    [[nodiscard]] std::vector<Oferta> sortByTipAndPret() const;

    //chestii de wishlist
    void adaugaInWishlist(const std::string& denumire);
    void golesteWishlist();
    void genereazaWishlist(int numar);
    [[nodiscard]] std::vector<Oferta> getAllWishlist() const;
    void exportCSV(const std::string& numeFisier) const;
    void importCSV(const std::string& numeFisier);

    [[nodiscard]] Oferta searchOferta(const std::string& denumire) const;
};

#endif //SERVICE_H
