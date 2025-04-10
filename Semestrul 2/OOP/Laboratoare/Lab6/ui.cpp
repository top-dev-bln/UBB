//
// Created by Balan Andrei Daniel on 03.04.2025.
//

#include <iostream>
#include "ui.h"


void UI::printMenu() {
    std::cout << "Alege o optiune:\n ";
    std::cout << "1. Adauga oferta\n";
    std::cout << "2. Modifica oferta\n";
    std::cout << "3. Șterge oferta\n";
    std::cout << "4. Afisare toate ofertele\n";
    std::cout << "5. Filtrare oferte\n";
    std::cout << "6. Sortare oferte\n";
    std::cout << "7. Cautare oferte\n";
    std::cout << "8. Exit\n";
    std::cout << ">>>>>> ";
}

void UI::uiAdd() {
    std::string denumire, tip;
    float distanta, pret;
    std::cout << "Introduceti denumirea ofertei: ";
    std::cin >> denumire;
    std::cout << "Introduceti tipul ofertei: ";
    std::cin >> tip;
    std::cout << "Introduceti distanta ofertei: ";
    std::cin >> distanta;
    std::cout << "Introduceti pretul ofertei: ";
    std::cin >> pret;

    servic.addOferta(denumire, tip, distanta, pret);
    std::cout << "Oferta adaugata cu succes!\n";
}

void UI::uiModify() {
    std::string denumire, tip;
    float distanta, pret;
    std::cout << "Introduceti denumirea ofertei: ";
    std::cin >> denumire;
    std::cout << "Introduceti tipul ofertei: ";
    std::cin >> tip;
    std::cout << "Introduceti distanta ofertei: ";
    std::cin >> distanta;
    std::cout << "Introduceti pretul ofertei: ";
    std::cin >> pret;

    servic.modifyOferta(denumire, tip, distanta, pret);
    std::cout << "Oferta modificata cu succes!\n";
}

void UI::uiDelete() {
    std::string denumire;
    std::cout << "Introduceti denumirea ofertei: ";
    std::cin >> denumire;

    servic.deleteOferta(denumire);
    std::cout << "Oferta stearsa cu succes!\n";
}

void UI::printAllOferte() {
    for (auto it = servic.begin(); it.valid(); it.next()) {
        const auto& oferta = it.element();
        std::cout << "Denumire: " << oferta.getDenumire()
                  << ", Tip: " << oferta.getTip()
                  << ", Distanta: " << oferta.getDistanta()
                  << ", Pret: " << oferta.getPret() << '\n';
    }
}

void UI::uiFilter() {
    char filterOpt;
    std::cout << "Filtrare dupa destinatie/pret\n";
    std::cout << "1. Filtrare dupa destinatie\n";
    std::cout << "2. Filtrare dupa pret\n";
    std::cin >> filterOpt;

    if (filterOpt == '1') {
        std::string destinatie;
        std::cout << "Introduceti destinatia: ";
        std::cin >> destinatie;
        auto filtered = servic.filterByDestinatie(destinatie);
        auto it = filtered.begin();
        while (it.valid()) {
            std::cout << "Denumire: " << it.element().getDenumire()
                      << ", Tip: " << it.element().getTip()
                      << ", Distanta: " << it.element().getDistanta()
                      << ", Pret: " << it.element().getPret() << '\n';
            it.next();
        }
    } else if (filterOpt == '2') {
        float pret;
        std::cout << "Introduceti pretul: ";
        std::cin >> pret;
        auto filtered = servic.filterByPret(pret);
        auto it = filtered.begin();
        while (it.valid()) {
            std::cout << "Denumire: " << it.element().getDenumire()
                      << ", Tip: " << it.element().getTip()
                      << ", Distanta: " << it.element().getDistanta()
                      << ", Pret: " << it.element().getPret() << '\n';
            it.next();
        }
    } else {
        std::cout << "Optiune invalida!\n";
    }
}
void UI::uiSort() {
    char sortOpt;
    std::cout << "Sortare dupa denumire/destinatie/tip+pret\n";
    std::cout << "1. Sortare dupa denumire\n";
    std::cout << "2. Sortare dupa destinatie\n";
    std::cout << "3. Sortare dupa tip+pret\n";
    std::cin >> sortOpt;

    VectorDinamic<Oferta> sorted;
    if (sortOpt == '1') {
        sorted = servic.sortByDenumire();
    } else if (sortOpt == '2') {
        sorted = servic.sortByDestinatie();
    } else if (sortOpt == '3') {
        sorted = servic.sortByTipAndPret();
    } else {
        std::cout << "Optiune invalida!\n";
        return;
    }

    auto it = sorted.begin();
    while (it.valid()) {
        std::cout << "Denumire: " << it.element().getDenumire()
                  << ", Tip: " << it.element().getTip()
                  << ", Distanta: " << it.element().getDistanta()
                  << ", Pret: " << it.element().getPret() << '\n';
        it.next();
    }
}

void UI::uiCauta() {
    std::string denumire;
    std::cout << "Introduceti denumirea ofertei: ";
    std::cin >> denumire;

    try {
        auto oferta = servic.searchOferta(denumire);
        std::cout << "Oferta gasita: Denumire: " << oferta.getDenumire()
                  << ", Tip: " << oferta.getTip()
                  << ", Distanta: " << oferta.getDistanta()
                  << ", Pret: " << oferta.getPret() << '\n';
    } catch (const std::exception& e) {
        std::cout << "Eroare: " << e.what() << '\n';
    }
}

void UI::run() {
    bool running = true;
    char opt;
    while (running) {
        printMenu();
        std::cin >> opt;

        switch (opt) {
            case '1':
                uiAdd();
                break;
            case '2':
                uiModify();
                break;
            case '3':
                uiDelete();
                break;
            case '4':
                printAllOferte();
                break;
            case '5':
                uiFilter();
                break;
            case '6':
                uiSort();
                break;
            case '7':
                uiCauta();
                break;
            case '8':
                running = false;
                break;
            default:
                std::cout << "Optiune invalida!\n";
        }
    }
}


