#include "wishlist.h"
#include <fstream>
#include <stdexcept>
#include <random>
#include <sstream>

void Wishlist::goleste() {
    cos.clear();
}

void Wishlist::adauga(const Oferta& oferta) {
    cos.push_back(oferta);
}


const std::vector<Oferta>& Wishlist::getToate() const {
    return cos;
}

void Wishlist::exportCSV(const std::string& numeFisier) const {
    std::ofstream fout(numeFisier);


    for (const auto& o : cos) {
        fout << o.getDenumire() << "," << o.getTip() << "," << o.getDistanta() << "," << o.getPret() << "\n";
    }

    fout.close();
}



void Wishlist::importCSV(const std::string& numeFisier) {
    std::ifstream fin(numeFisier);


    std::string linie;
    while (std::getline(fin, linie)) {
        std::stringstream ss(linie);
        std::string denumire, tip, distantaStr, pretStr;

        std::getline(ss, denumire, ',');
        std::getline(ss, tip, ',');
        std::getline(ss, distantaStr, ',');
        std::getline(ss, pretStr, ',');


        float distanta = std::stof(distantaStr);
        float pret = std::stof(pretStr);

        Oferta o(denumire, tip, distanta, pret);
        cos.push_back(o);
    }

    fin.close();
}