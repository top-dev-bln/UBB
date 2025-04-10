#include "VectorDinamic.h"
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
    capacitate = 10;
    lungime = 0;
    elems = new T[capacitate];
}

template <typename T>
VectorDinamic<T>::~VectorDinamic() {
    delete[] elems;
}

template <typename T>
void VectorDinamic<T>::erase(IteratorVector<T>& it) {
    if (!it.valid()) {
        throw std::out_of_range("Iterator invalid!");
    }

    for (int i = it.poz; i < lungime - 1; i++) {
        elems[i] = elems[i + 1];
    }

    lungime--;

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
    if (index < 0 || index >= lungime) {
        throw std::out_of_range("Index invalid");
    }
    return elems[index];
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
    return poz < v.lungime;
}

template <typename T>
void IteratorVector<T>::next() {
    if (!valid()) {
        throw std::out_of_range("Iterator a zburat!");
    }
    ++poz;
}

template <typename T>
T IteratorVector<T>::element() const {
    if (!valid()) {
        throw std::out_of_range("Iterator invalid!");
    }
    return v.get_element(poz);
}

