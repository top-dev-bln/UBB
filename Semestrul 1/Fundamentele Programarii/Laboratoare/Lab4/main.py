from offer import Package



class package_processor:

    def meniu(self, menu:int=0)->str:
        menus={
            0:'''
1. Adaugare
2. Stergere
3. Cautare
4. Rapoarte
5. Filtrare
6. Undo

9. Exit
''',
            1:'''
1. Adaugare pachet
2. Modificare pachet existent
3. Undo


9. Back
''',
            2:'''
1. Stergere pachete dupa destinatie
2. Stergere pachete dupa durata
3. Stergere pachete dupa pret
4. Undo

9. Back
''',
            3:'''
1. Afisare pachete intr-un interval
2. Afisare pachete cu destinatie si pret sub stabilit
3. Afisare pachete dupa data de sfarsit


9. Back
''',
            4:'''
1. Afisare numarul de oferte pentru o destinatie
2. Afisare tuturor pachetelor disponibile intr-un interval (crescator dupa pret)
3. Afisare mediei de pret pentru o destinatie


9. Back
''',
            5:'''
1. Eliminare oferte peste buget sau destinatie diferita
2. Eliminare oferte ce presupun zile dintr-o anumita luna


9. Back
'''

        }

        return menus[menu]


    

    def run(self)->None:
        print(self.meniu())
        





process = package_processor()
process.run()
