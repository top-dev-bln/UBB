from offer import Package
import os
from datetime import datetime



class package_processor:


    
    def __init__(self) -> None:
        """
        Initializează clasa package_processor.

        Setează atributul __running la False, inițializează lista de oferte __offers ca fiind goală, 
        definește un dicționar __submenu_functions care mapează ID-urile submeniurilor la dicționare 
        ce conțin funcțiile corespunzătoare fiecărei opțiuni din submeniu, și definește un dicționar meniu 
        care conține string-urile ce vor fi afișate pentru fiecare meniu.
        """
        self.__running = False
        self.__offers = []
        self.__submenu_functions = {
            1: {1: self.add_package, 2: self.modify_package, 3: self.handle_undo},  # Add Menu
            2: {1: self.delete_by_destination, 2: self.delete_by_duration, 3: self.delete_by_price, 4: self.handle_undo},  # Delete Menu
            3: {1: self.search_by_interval, 2: self.search_by_destination_price, 3: self.search_by_end_date},  # Search Menu
            4: {1: self.report_offer_count, 2: self.report_packages_in_interval, 3: self.report_avg_price},  # Report Menu
            5: {1: self.filter_by_budget, 2: self.filter_by_month},  # Filter Menu
        }
        self.meniu={
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
        
        #todo4 remove after testing
        self.__offers.append(Package(datetime(2024, 5, 16), datetime(2024, 6, 15), "garden", 100))
        self.__offers.append(Package(datetime(2024, 7, 2), datetime(2024, 7, 12), "manastur", 87))
        self.__offers.append(Package(datetime(2024, 5, 12), datetime(2024, 8, 12), "rwanda", 420))
        self.__offers.append(Package(datetime(2024, 5, 12), datetime(2024, 9, 12), "manastur", 69))
        
    def fuzzy_search_destination(self, query:str)->str:
         """
         Caută o destinație folosind căutare fuzzy.
         """
         destinations = [offer.get_destination() for offer in self.__offers]
         import difflib

         matches = difflib.get_close_matches(query, destinations, n=1, cutoff=0.6)
         if matches:
             return matches[0]
         else:
             return None

    def handle_undo(self):
        print("\033[32mUndo realizat cu succes\033[0m") 

    def get_date(self):
        """
        Obține de la utilizator datele de început și de sfârșit ale unei perioade, asigurându-se că sunt valide și că data de început este înaintea datei de sfârșit.
        Returns:
            list: O listă care conține două obiecte datetime, reprezentând data de început și data de sfârșit.
        """
        data=[]
        labels = ["inceput", "sfarsit"]
        while True:
            for label in labels:
                while True:
                    try:
                        print(f"Introduceti data de {label}")
                        ziua=int(input("Ziua: "))
                        if ziua<1 or ziua>31:
                            raise ValueError("Ziua invalida")
                        luna=int(input("Luna: "))
                        if luna<1 or luna>12:
                            raise ValueError("Luna invalida")
                        anul=int(input("Anul: "))
                        if anul<1:
                            raise ValueError("Anul invalid")
                        data.append(datetime(anul, luna, ziua))
                        break
                    except ValueError as e:
                        print(f"\033[31m{e}\033[0m")
            if(data[0]>data[1]):
                os.system("cls")
                print("Data de inceput trebuie sa fie inaintea data de sfarsit")
                data.pop()
                continue
            else:
                return data


    def add_package(self):
        print("\033[33mAdaugare pachet nou\033[0m")
        data=self.get_date()
        destination=str(input("Destinatie: "))
        price=float(input("Pret: "))

        self.__offers.append(Package(data[0], data[1], destination, price))
        
        print("\033[32mPachet adaugat cu succes\033[0m") 
        print(str(self.__offers[-1]))


 
    def modify_package(self):
        print("\033[33mModificare pachet\033[0m")
        print("Ce pachet doriti sa modificati?")
        for i, offer in enumerate(self.__offers):
            print(f"{i+1}. {offer}")
        id = int(input("=> ")) 

        pachet=self.__offers[id-1]
        data=self.get_date()
        destination=str(input("Destinatie: "))
        price=float(input("Pret: "))
        pachet.start_date=data[0]
        pachet.end_date=data[1]
        pachet.destination=destination
        pachet.price=price
        self.__offers[id-1]=pachet
        print("\033[32mPachet modificat cu succes\033[0m")
        print(str(pachet))


    
    # Delete

    def delete_by_destination(self):
        """
        Șterge toate ofertele cu o anumită destinație.
        """
        destination = input("Introduceți destinația de șters: ")
        fuzzy_destination = self.fuzzy_search_destination(destination)
        if fuzzy_destination:
            print(f"Did you mean '{fuzzy_destination}'?")
            confirm = input("Yes/No: ")
            if confirm.lower() == 'yes':
                destination = fuzzy_destination
        self.__offers = [offer for offer in self.__offers if offer.get_destination() != destination]
        print(f"Toate ofertele cu destinația '{destination}' au fost șterse.")

    def delete_by_duration(self):
        print("Deleting package by duration")

    def delete_by_price(self):
        print("Deleting package by price")

    # Search

    def search_by_interval(self):
        print("Searching packages in interval")

    def search_by_destination_price(self):
        print("Searching packages by destination and price")

    def search_by_end_date(self):
        print("Searching packages by end date")

    # Report

    def report_offer_count(self):
        print("Reporting number of offers for a destination")

    def report_packages_in_interval(self):
        print("Reporting packages in an interval")

    def report_avg_price(self):
        print("Reporting average price for a destination")

    # Filter

    def filter_by_budget(self):
        print("Filtering offers by budget")

    def filter_by_month(self):
        print("Filtering offers by month")



        





        
    def menu_handler(self, menu_id: int)->None:
        """
        Gestionează afișarea meniurilor și execuția funcțiilor corespunzătoare opțiunilor alese de utilizator.

        Args:
            menu_id (int): ID-ul meniului care trebuie afișat. 0 reprezintă meniul principal, iar valorile de la 1 la 5 reprezintă submeniurile.
        """
        while self.__running:
            print(self.meniu[menu_id])
            try:
                option = int(input("Alegeti o optiune: "))

                if menu_id == 0:
                    if 1 <= option <= 5:
                        os.system("cls")
                        self.menu_handler(option)
                    elif option == 9:
                        self.__running = False
                        os.system("cls")
                        break
                    else:
                        raise ValueError("Optiune invalida in meniul principal.")

                elif menu_id != 0:
                    if option == 9:
                        os.system("cls")
                        break
                    elif 1 <= option <= len(self.__submenu_functions[menu_id]):
                        os.system("cls")
                        self.__submenu_functions[menu_id][option]()
                    else:
                        print("Optiune invalida in meniu.")

            except ValueError:
                print("Introduceti un numar valid.")



    def run(self)->None:
        """
        Pornește bucla principală a aplicației.
        
        Curăță consola, setează semnalizatorul de rulare la True și apoi apelează gestionarul de meniu pentru a afișa meniul principal.
        """
        os.system("cls")
        self.__running = True
        self.menu_handler(0)  



process = package_processor()
process.run()
