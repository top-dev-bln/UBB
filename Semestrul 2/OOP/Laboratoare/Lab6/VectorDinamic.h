#ifndef VECTORDINAMIC_H
#define VECTORDINAMIC_H

#pragma once

template <typename T>
class IteratorVector;

template <typename T>
class VectorDinamic {
private:
    T* elems;
    int capacitate;
    int lungime;

    void resize();

public:
    VectorDinamic();
    ~VectorDinamic();
    void push_back(const T& obiect);
    int size() const;
    void erase(IteratorVector<T>& it);
    [[nodiscard]] int get_lungime() const { return lungime; }
    [[nodiscard]] int get_capacitate() const { return capacitate; }
    T get_element(int index) const;
    friend class IteratorVector<T>;
    IteratorVector<T> begin() const;
    IteratorVector<T> end() const;
};

template <typename T>
class IteratorVector {
private:
    const VectorDinamic<T>& v;
    int poz;

public:
    IteratorVector(const VectorDinamic<T>& vec, int pozitie);
    bool valid() const;
    [[nodiscard]] int get_poz() const { return poz; }
    void next();
    T& element() const;
};

#include <stdexcept>

template <typename T>
void VectorDinamic<T>::resize() {
    int nouaCapacitate = capacitate * 2;
    T* nouElems = new T[nouaCapacitate];
    for (int i = 0; i < lungime; i++) {
        nouElems[i] = elems[i];
    }
    delete[] elems;
    elems = nouElems;
    capacitate = nouaCapacitate;
}

template <typename T>
VectorDinamic<T>::VectorDinamic() {
    capacitate = 1;
    lungime = 0;
    elems = new T[capacitate];
}

template <typename T>
VectorDinamic<T>::~VectorDinamic() {
    delete[] elems;
}

template <typename T>
void VectorDinamic<T>::erase(IteratorVector<T>& it) {
    if (it.valid()) {
        for (int i = it.get_poz(); i < lungime - 1; i++) {
            elems[i] = elems[i + 1];
        }
        lungime--;
    }

}

template <typename T>
void VectorDinamic<T>::push_back(const T& obiect) {
    if (lungime == capacitate) {
        resize();
    }
    elems[lungime++] = obiect;
}

template <typename T>
int VectorDinamic<T>::size() const {
    return lungime;
}

template <typename T>
[[nodiscard]] T VectorDinamic<T>::get_element(int index) const {
    if (index >=0 && index < lungime) {
        return elems[index];
    }

}

template <typename T>
IteratorVector<T> VectorDinamic<T>::begin() const {
    return IteratorVector<T>(*this, 0);
}

template <typename T>
IteratorVector<T> VectorDinamic<T>::end() const {
    return IteratorVector<T>(*this, lungime);
}

template <typename T>
IteratorVector<T>::IteratorVector(const VectorDinamic<T>& vec, int pozitie) : v(vec), poz(pozitie) {}

template <typename T>
bool IteratorVector<T>::valid() const {
    return get_poz() < v.get_lungime();
}

template <typename T>
void IteratorVector<T>::next() {
    if (valid()) {
        ++poz;
    }

}

template <typename T>
T& IteratorVector<T>::element() const {
    if (valid()) {
        return v.elems[poz];
    }

}

#endif //VECTORDINAMIC_H