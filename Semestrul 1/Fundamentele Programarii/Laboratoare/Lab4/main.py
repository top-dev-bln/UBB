from offer import Package
import os



class package_processor:


    
    def __init__(self) -> None:
        self.__running = False

        self.__offers = []

        self.__submenu_functions = {
            1: {1: self.add_package, 2: self.modify_package, 3: self.handle_undo},  # Add Menu
            2: {1: self.delete_by_destination, 2: self.delete_by_duration, 3: self.delete_by_price, 4: self.handle_undo},  # Delete Menu
            3: {1: self.search_by_interval, 2: self.search_by_destination_price, 3: self.search_by_end_date},  # Search Menu
            4: {1: self.report_offer_count, 2: self.report_packages_in_interval, 3: self.report_avg_price},  # Report Menu
            5: {1: self.filter_by_budget, 2: self.filter_by_month},  # Filter Menu
        }
    

    def handle_undo(self):
        print("Undo")



    # Submenu functions

    # Add
    def add_package(self):
        print(f"\033[33mAdaugare pachet nou\033[0m")
        start=int(input("Data de inceput: "))
        end=int(input("Data de sfarsit: "))
        destination=str(input("Destinatie: "))
        price=float(input("Pret: "))

        self.__offers.append(Package(start, end, destination, price))
        print(f"\033[32mPachet adaugat cu succes\033[0m")

    def modify_package(self):
        print("Modifying existing package")
    
    # Delete

    def delete_by_destination(self):
        print("Deleting package by destination")

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
        
    def menu_handler(self, menu_id: int):
        while self.__running:
            print(self.meniu(menu_id))
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
        os.system("cls")
        self.__running = True
        self.menu_handler(0)  



process = package_processor()
process.run()
