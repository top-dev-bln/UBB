//
// Created by Balan Andrei Daniel on 06.04.2025.
//

#ifndef VALIDATOR_H
#define VALIDATOR_H


#include "repository.h"



class Validator {
private:
    Repository& repository;

public:
    bool isValidDenumire(const std::string& denumire) const;
    bool isValidTip(const std::string& tip);
    bool isValidDistanta(float distanta);
    bool isValidPret(float pret) const;
    bool isrepetata(const std::string& denumire, const std::string& tip, float distanta, float pret);
    bool isExista(const std::string& denumire);


    explicit Validator(Repository& repo) : repository(repo) {}
    ~Validator();


};



#endif //VALIDATOR_H
