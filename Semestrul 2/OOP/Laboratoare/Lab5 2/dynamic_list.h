#ifndef DYNAMIC_LIST_H
#define DYNAMIC_LIST_H

typedef struct {
    void** elements;
    int size;
    int capacity;
} DynamicList;

DynamicList* CreateDynamicList();
void AddToList(DynamicList* list, void* element);
void* GetFromList(DynamicList* list, int index);
void RemoveFromList(DynamicList* list, int index, void (*freeElement)(void*));
void FreeDynamicList(DynamicList* list, void (*freeElement)(void*));

#endif // DYNAMIC_LIST_H
