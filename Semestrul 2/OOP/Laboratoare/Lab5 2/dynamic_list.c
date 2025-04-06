#include "dynamic_list.h"
#include <stdlib.h>

DynamicList* CreateDynamicList() {
    DynamicList* list = (DynamicList*)malloc(sizeof(DynamicList));
    list->capacity = 2;
    list->size = 0;
    list->elements = (void**)malloc(list->capacity * sizeof(void*));
    return list;
}

void AddToList(DynamicList* list, void* element) {
    if (list->size == list->capacity) {
        list->capacity *= 2;
        list->elements = (void**)realloc(list->elements, list->capacity * sizeof(void*));
    }
    list->elements[list->size++] = element;
}

void* GetFromList(DynamicList* list, int index) {
    if (index < 0 || index >= list->size) {
        return NULL;
    }
    return list->elements[index];
}

void RemoveFromList(DynamicList* list, int index, void (*freeElement)(void*)) {
    if (index < 0 || index >= list->size) {
        return;
    }
    if (freeElement) {
        freeElement(list->elements[index]);
    }
    for (int i = index; i < list->size - 1; i++) {
        list->elements[i] = list->elements[i + 1];
    }
    list->size--;
}

void FreeDynamicList(DynamicList* list, void (*freeElement)(void*)) {
    if (freeElement) {
        for (int i = 0; i < list->size; i++) {
            freeElement(list->elements[i]);
        }
    }
    free(list->elements);
    free(list);
}
