//
// Created by Balan Andrei Daniel on 03.04.2025.
//

#ifndef UI_H
#define UI_H

#include "service.h"

class UI {
private:
    Service& servic;

    void printMenu();
    void uiAdd();
    void uiModify();
    void uiDelete();
    void printAllOferte();
    void uiFilter();
    void uiSort();
    void uiCauta();
    void uiWishlist();
    void emptywishlist();
    void generatewishlist();
    void addwithlist();
    void printwishlist();
    void exportwishlist();
    void importwishlist();


public:
    explicit UI(Service& service) : servic(service) {}
    void run();
};

#endif //UI_H
