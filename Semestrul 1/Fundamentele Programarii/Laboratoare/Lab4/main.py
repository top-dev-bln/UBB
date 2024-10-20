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
            2: {1: self.delete_by_destination, 2: self.delete_between_dates, 3: self.delete_by_price, 4: self.handle_undo},  # Delete Menu
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
    
    #todo testing for fuzzy search
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

    
    def add_package(self)->None:
        """
        Adaugă o ofertă nouă în lista de oferte.
        """
        data=self.get_date()
        destination = input("Introduceti destinatia: ")
        while True:
            try:
                price = float(input("Introduceti pretul: "))
                if price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Pret invalid. Va rugam introduceti un numar pozitiv.")
        offer = Package(data[0], data[1], destination, price)
        self.__offers.append(offer)
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

    def delete_by_destination(self)->None:
        """
        Sterge ofertele cu o destinație dată.
        """
        destination = input("Introduceți destinația de șters: ")
        fuzzy_destination = self.fuzzy_search_destination(destination)
        if fuzzy_destination is None:
            print("Nu s-a gasit nicio destinatie similara.")
            return
        self.__offers = [offer for offer in self.__offers if offer.get_destination() != fuzzy_destination]

        print(f"Ofertele cu destinația {fuzzy_destination} au fost șterse.")



    def delete_by_destination_simple(self)->None:
        """
        Sterge ofertele cu o destinație exactă dată.
        """
        destination = input("Introduceți destinația exactă de șters: ")
        initial_count = len(self.__offers)
        self.__offers = [offer for offer in self.__offers if offer.get_destination().lower() != destination.lower()]
        deleted_count = initial_count - len(self.__offers)
        
        if deleted_count > 0:
            print(f"{deleted_count} oferte cu destinația {destination} au fost șterse.")
        else:
            print(f"Nu s-au găsit oferte cu destinația exactă {destination}.")

        
    def delete_by_price(self)->None:
        """
        Sterge ofertele care au un pret mai mare decat cel dat.
        """
        while True:
            try:
                price = float(input("Introduceți prețul maxim: "))
                if price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Preț invalid. Va rugam introduceti un numar pozitiv.")
        self.__offers = [offer for offer in self.__offers if offer.price <= price]
        print(f"Ofertele cu prețul mai mare de {price} Euro au fost șterse.")


    def delete_between_dates(self)->None:
        """
        Sterge ofertele dintr-un interval de date dat.
        """
        start_date = self.get_date()
        end_date = self.get_date()
        self.__offers = [offer for offer in self.__offers if not (start_date <= offer.start_date <= end_date)]
        print(f"Ofertele din intervalul {start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')} au fost șterse.")

    def increase_price(self)->None:
        """
        Mărește prețul ofertelor cu o destinație dată cu un procent dat.
        """
        destination = input("Introduceți destinația pentru care se mărește prețul: ")
        fuzzy_destination = self.fuzzy_search_destination(destination)
        if fuzzy_destination is None:
            print("Nu s-a gasit nicio destinatie similara.")
            return
        while True:
            try:
                percentage = float(input("Introduceți procentul cu care se mărește prețul: "))
                if percentage <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Procent invalid. Va rugam introduceti un numar pozitiv.")
        for offer in self.__offers:
            if offer.get_destination() == fuzzy_destination:
                offer.price *= (1 + percentage / 100)
        print(f"Prețul ofertelor cu destinația {fuzzy_destination} a fost mărit cu {percentage}%.")

    def decrease_price(self)->None:
        """
        Micșorează prețul ofertelor cu o destinație dată cu un procent dat.
        """
        destination = input("Introduceți destinația pentru care se micșorează prețul: ")
        fuzzy_destination = self.fuzzy_search_destination(destination)
        if fuzzy_destination is None:
            print("Nu s-a gasit nicio destinatie similara.")
            return
        while True:
            try:
                percentage = float(input("Introduceți procentul cu care se micșorează prețul: "))
                if percentage <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Procent invalid. Va rugam introduceti un numar pozitiv.")
        for offer in self.__offers:
            if offer.get_destination() == fuzzy_destination:
                offer.price *= (1 - percentage / 100)
        print(f"Prețul ofertelor cu destinația {fuzzy_destination} a fost micșorat cu {percentage}%.")

    def print_all_offers(self)->None:
        """
        Afișează toate ofertele din lista de oferte.
        """
        if not self.__offers:
            print("Nu există oferte disponibile.")
            return
        for offer in self.__offers:
            print(offer)

    def print_by_destination(self)->None:
        """
        Afișează ofertele cu o destinație dată.
        """
        destination = input("Introduceți destinația: ")
        fuzzy_destination = self.fuzzy_search_destination(destination)
        if fuzzy_destination is None:
            print("Nu s-a gasit nicio destinatie similara.")
            return
        found = False
        for offer in self.__offers:
            if offer.get_destination() == fuzzy_destination:
                print(offer)
                found = True
        if not found:
            print(f"Nu există oferte cu destinația {fuzzy_destination}.")

    def print_cheaper_than(self)->None:
        """
        Afișează ofertele mai ieftine decât un preț dat.
        """
        while True:
            try:
                price = float(input("Introduceți prețul maxim: "))
                if price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Preț invalid. Va rugam introduceti un numar pozitiv.")
        found = False
        for offer in self.__offers:
            if offer.price < price:
                print(offer)
                found = True
        if not found:
            print(f"Nu există oferte mai ieftine decât {price} Euro.")

    def search_by_interval(self):
        """
        Cauta pachete in functie de un interval de timp dat.
        """
        print("\033[33mCautare pachete in functie de un interval de timp dat\033[0m")
        data = self.get_date()
        gasit = False
        for offer in self.__offers:
            if data[0] <= offer.start_date <= data[1]:
                print(offer)
                gasit = True
        if not gasit:
            print(f"Nu exista pachete in intervalul {data[0].strftime('%Y-%m-%d')} - {data[1].strftime('%Y-%m-%d')}.")

    def search_by_destination_price(self):
        """
        Cauta pachete in functie de destinatie si pret maxim.
        """
        print("\033[33mCautare pachete in functie de destinatie si pret maxim\033[0m")
        destination = input("Introduceti destinatia: ")
        max_price = float(input("Introduceti pretul maxim: "))
        gasit = False
        for offer in self.__offers:
            if offer.destination == destination and offer.price <= max_price:
                print(offer)
                gasit = True
        if not gasit:
            print(f"Nu exista pachete cu destinatia {destination} si pretul mai mic sau egal cu {max_price}.")

    def search_by_end_date(self):
        """
        Cauta pachete in functie de data de sfarsit.
        """
        print("\033[33mCautare pachete in functie de data de sfarsit\033[0m")
        while True:
            try:
                print("Introduceti data de sfarsit")
                ziua = int(input("Ziua: "))
                if ziua < 1 or ziua > 31:
                    raise ValueError("Ziua invalida")
                luna = int(input("Luna: "))
                if luna < 1 or luna > 12:
                    raise ValueError("Luna invalida")
                anul = int(input("Anul: "))
                if anul < 1:
                    raise ValueError("Anul invalid")
                end_date = datetime(anul, luna, ziua)
                break
            except ValueError as e:
                print(f"\033[31m{e}\033[0m")
        gasit = False
        for offer in self.__offers:
            if offer.end_date <= end_date:
                print(offer)
                gasit = True
        if not gasit:
            print(f"Nu exista pachete cu data de sfarsit inainte de {end_date.strftime('%Y-%m-%d')}.")

    def report_offer_count(self):
        """
        Afiseaza numarul de oferte pentru o destinatie data.
        """
        print("\033[33mAfisare numar de oferte pentru o destinatie\033[0m")
        destination = input("Introduceti destinatia: ")
        count = 0
        for offer in self.__offers:
            if offer.destination == destination:
                count += 1
        if count == 0:
            print(f"Nu exista oferte pentru destinatia {destination}.")
        else:
            print(f"Exista {count} oferte pentru destinatia {destination}.")

    def report_packages_in_interval(self):
        """
        Afiseaza toate pachetele disponibile intr-un interval de timp dat, sortate crescator dupa pret.
        """
        print("\033[33mAfisare pachete disponibile intr-un interval de timp\033[0m")
        data = self.get_date()
        filtered_offers = [
            offer for offer in self.__offers if data[0] <= offer.start_date <= data[1]
        ]
        filtered_offers.sort(key=lambda offer: offer.price)
        if not filtered_offers:
            print(
                f"Nu exista pachete in intervalul {data[0].strftime('%Y-%m-%d')} - {data[1].strftime('%Y-%m-%d')}."
            )
        else:
            for offer in filtered_offers:
                print(offer)

    def report_avg_price(self):
        """
        Afiseaza pretul mediu pentru o destinatie data.
        """
        print("\033[33mAfisare pret mediu pentru o destinatie\033[0m")
        destination = input("Introduceti destinatia: ")
        prices = [offer.price for offer in self.__offers if offer.destination == destination]
        if not prices:
            print(f"Nu exista oferte pentru destinatia {destination}.")
        else:
            avg_price = sum(prices) / len(prices)
            print(f"Pretul mediu pentru destinatia {destination} este {avg_price:.2f} Euro.")

    def filter_by_budget(self):
        """
        Elimina ofertele care depasesc un buget dat sau au o destinatie diferita de cea data.
        """
        print("\033[33mEliminare oferte peste buget sau destinatie diferita\033[0m")
        budget = float(input("Introduceti bugetul: "))
        destination = input("Introduceti destinatia: ")
        initial_count = len(self.__offers)
        self.__offers = [
            offer for offer in self.__offers if offer.price <= budget and offer.destination == destination
        ]
        removed_count = initial_count - len(self.__offers)
        print(f"Au fost eliminate {removed_count} oferte.")


    def print_between_dates(self)->None:
        """
        Afișează ofertele dintr-un interval de date dat.
        """
        start_date = self.get_date()
        end_date = self.get_date()
        found = False
        for offer in self.__offers:
            if start_date <= offer.start_date <= end_date:
                print(offer)
                found = True
        if not found:
            print(f"Nu există oferte în intervalul {start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}.")

    def filter_by_month(self)->None:
        """
        Elimina ofertele care depasesc un lună dat sau au o destinatie diferita de cea data.
        """
        print("\033[33mEliminare oferte peste lună sau destinatie diferita\033[0m")
        month = int(input("Introduceti luna: "))
        if month < 1 or month > 12:
            print("Luna invalida.")
            return
        destination = input("Introduceti destinatia: ")
        initial_count = len(self.__offers)
        self.__offers = [
            offer for offer in self.__offers if offer.start_date.month == month and offer.destination == destination
        ]
        removed_count = initial_count - len(self.__offers)
        print(f"Au fost eliminate {removed_count} oferte.")
        

    





        
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
