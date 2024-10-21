import os
from datetime import datetime, timedelta
from package import Package
from utils import get_date, fuzzy_search_destination

class PackageManager:
    def __init__(self):
        self.__offers = []
        self.__history = []
        self.__running = False
        self.__submenu_functions = {
            1: {1: self.add_package_interactive, 2: self.modify_package, 3: self.handle_undo},  # Add Menu
            2: {1: self.delete_by_destination, 2: self.delete_by_duration, 3: self.delete_by_price, 4: self.handle_undo},  # Delete Menu
            3: {1: self.search_by_interval, 2: self.search_by_destination_price, 3: self.search_by_end_date},  # Search Menu
            4: {1: self.report_offer_count, 2: self.report_packages_in_interval, 3: self.report_avg_price},  # Report Menu
            5: {1: self.search_by_destination_price, 2: self.filter_by_month},  # Filter Menu
        }
        self.meniu = {
            0: '''
1. Adaugare
2. Stergere
3. Cautare
4. Rapoarte
5. Filtrare
6. Undo

9. Exit
''',
            1: '''
1. Adaugare pachet
2. Modificare pachet existent
3. Undo

9. Back
''',
            2: '''
1. Stergere pachete dupa destinatie
2. Stergere pachete dupa durata
3. Stergere pachete dupa pret
4. Undo

9. Back
''',
            3: '''
1. Afisare pachete intr-un interval
2. Afisare pachete cu destinatie si pret sub stabilit
3. Afisare pachete dupa data de sfarsit

9. Back
''',
            4: '''
1. Afisare numarul de oferte pentru o destinatie
2. Afisare tuturor pachetelor disponibile intr-un interval (crescator dupa pret)
3. Afisare mediei de pret pentru o destinatie

9. Back
''',
            5: '''
1. Eliminare oferte peste buget sau destinatie diferita
2. Eliminare oferte ce presupun zile dintr-o anumita luna

9. Back
'''
        }

    def __record_change(self, change_type:str, packages:list, previous:Package=None):
        self.__history.append({
            'type': change_type,
            'packages': packages,
            'previous': previous,
        })

    def handle_undo(self):
        if not self.__history:
            print("\033[31mNu se poate realiza undo. Nu există o stare anterioară disponibilă.\033[0m")
            return

        last_change = self.__history.pop() 
        change_type = last_change['type']

        if change_type == 'add':
            self.__offers.remove(last_change['packages'][0])
        elif change_type == 'delete':
            for package in last_change['packages']:
                self.__offers.append(package)
            print(f"Restored {len(last_change['packages'])} package(s)")
        elif change_type == 'modify':
            index = self.__offers.index(last_change['packages'][0])
            self.__offers[index] = last_change['previous']

        print("\033[32mUndo realizat cu succes\033[0m")

    def get_package_data(self):
        data = get_date()
        destination = input("Introduceti destinatia: ")
        while True:
            try:
                price = float(input("Introduceti pretul: "))
                if price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Pret invalid. Va rugam introduceti un numar pozitiv.")
        return data[0], data[1], destination, price

    def add_package(self, start_date, end_date, destination, price):
        new_package = Package(start_date, end_date, destination, price)
        self.__offers.append(new_package)
        self.__record_change('add', [new_package])
        print("\033[32mPachet adaugat cu succes\033[0m") 
        print(str(new_package))

    def add_package_interactive(self):
        start_date, end_date, destination, price = self.get_package_data()
        self.add_package(start_date, end_date, destination, price)

    def modify_package(self):
        print("\033[33mModificare pachet\033[0m")
        if not self.__offers:
            print("Nu exista pachete disponibile pentru modificare.")
            return
        print("Ce pachet doriti sa modificati?")
            
        for i, offer in enumerate(self.__offers):
            print(f"{i+1}. {offer}")
        id = int(input("=> ")) - 1

        if id < 0 or id >= len(self.__offers):
            print("Id-ul introdus este invalid.")
            return
        
        previous_package = self.__offers[id]
        new_data = get_date()
        destination = input("Destinatie: ")
        price = float(input("Pret: "))
        new_package = Package(new_data[0], new_data[1], destination, price)
        self.__offers[id] = new_package
        self.__record_change('modify', [new_package], previous_package)
        print("\033[32mPachet modificat cu succes\033[0m")

    def delete_by_destination(self):
        destination = input("Introduceți destinația de șters: ")
        fuzzy_destination = fuzzy_search_destination(destination, [offer.destination for offer in self.__offers])
        if fuzzy_destination is None:
            print("Nu s-a gasit nicio destinatie similara.")
            return
        if destination != fuzzy_destination:
            print(f"ai vrut sa spui {fuzzy_destination}")
            valid = input("Da sau Nu?  => ")
            if valid[0].lower() != "d":
                return
            
        removed_offers = [offer for offer in self.__offers if offer.destination == fuzzy_destination]
        if removed_offers:
            self.__record_change('delete', removed_offers)
            self.__offers = [offer for offer in self.__offers if offer not in removed_offers]
            print(f"Am șters {len(removed_offers)} oferte cu destinația {fuzzy_destination}.")
        else:
            print(f"Nu există oferte cu destinația {fuzzy_destination}.")

    def delete_by_duration(self):
        duration = int(input("Introduceți durata de timp ( in zile ):  => "))
        if duration < 1:
            print("Durata invalidă")
            return
        
        removed_offers = [offer for offer in self.__offers if offer.end_date - offer.start_date > timedelta(days=duration)]
        if removed_offers:
            self.__record_change('delete', removed_offers)
            self.__offers = [offer for offer in self.__offers if offer not in removed_offers]
            print(f"Ofertele cu durata de timp mai mică sau egală cu {duration} zile au fost șterse.")
        else:
            print(f"Nu există oferte cu durata de timp mai mică sau egală cu {duration} zile.")

    def delete_by_price(self):
        while True:
            try:
                price = float(input("Introduceți prețul maxim: "))
                if price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Preț invalid. Va rugam introduceti un numar pozitiv.")

        removed_offers = [offer for offer in self.__offers if offer.price > price]
        if removed_offers:
            self.__record_change('delete', removed_offers)
            self.__offers = [offer for offer in self.__offers if offer not in removed_offers]
            print(f"Ofertele cu prețul mai mare de {price} Euro au fost șterse.")
        else:
            print(f"Nu există oferte cu prețul mai mare de {price} Euro.")

    def search_by_interval(self):
        print("\033[33mCautare pachete in functie de un interval de timp dat\033[0m")
        data = get_date()
        gasit = False
        for offer in self.__offers:
            if data[0] <= offer.start_date <= data[1]:
                print(offer)
                gasit = True
        if not gasit:
            print(f"Nu exista pachete in intervalul {data[0].strftime('%Y-%m-%d')} - {data[1].strftime('%Y-%m-%d')}.")

    def search_by_destination_price(self):
        print("\033[33mCautare pachete in functie de destinatie si pret maxim\033[0m")
        max_price = float(input("Introduceti pretul maxim: "))
        destination = input("Introduceți destinația: ")
        fuzzy_destination = fuzzy_search_destination(destination, [offer.destination for offer in self.__offers])
        if fuzzy_destination is None:
            print("Nu s-a gasit nicio destinatie similara.")
            return
        
        if destination != fuzzy_destination:
            print(f"ai vrut sa spui {fuzzy_destination}")
            valid = input("Da sau Nu?  => ")
            if valid[0].lower() != "d":
                return
        gasit = False
        for offer in self.__offers:
            if offer.destination == fuzzy_destination and offer.price < max_price:
                print(offer)
                gasit = True
        if not gasit:
            print(f"Nu exista pachete cu destinatia {fuzzy_destination} si pretul mai mic sau egal cu {max_price}.")

    def search_by_end_date(self):
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
            if offer.end_date == end_date:
                print(offer)
                gasit = True
        if not gasit:
            print(f"Nu exista pachete cu data de sfarsit inainte de {end_date.strftime('%Y-%m-%d')}.")

    def report_offer_count(self):
        print("\033[33mAfisare numar de oferte pentru o destinatie\033[0m")
        destination = input("Introduceti o destinatie: ")
        fuzzy_destination = fuzzy_search_destination(destination, [offer.destination for offer in self.__offers])
        if fuzzy_destination is None:
            print("Nu s-a gasit nicio destinatie similara.")
            return
        if destination != fuzzy_destination:
            print(f"ai vrut sa spui {fuzzy_destination}")
            valid = input("Da sau Nu?  => ")
            if valid[0].lower() != "d":
                return 
        count = sum(1 for offer in self.__offers if offer.destination == fuzzy_destination)
        if count == 0:
            print(f"Nu exista oferte pentru destinatia {fuzzy_destination}.")
        else:
            print(f"Exista {count} oferte pentru destinatia {fuzzy_destination}.")

    def report_packages_in_interval(self):
        print("\033[33mAfisare pachete disponibile intr-un interval de timp\033[0m")
        data = get_date()
        filtered_offers = [offer for offer in self.__offers if data[0] <= offer.start_date <= data[1]]
        
        if not filtered_offers:
            print(f"Nu exista pachete in intervalul {data[0].strftime('%Y-%m-%d')} - {data[1].strftime('%Y-%m-%d')}.")
        else:
            filtered_offers.sort(key=lambda offer: offer.price)
            for offer in filtered_offers:
                print(offer)

    def report_avg_price(self):
        print("\033[33mAfisare pret mediu pentru o destinatie\033[0m")
        destination = input("Introduceti destinatia: ")
        fuzzy_destination = fuzzy_search_destination(destination, [offer.destination for offer in self.__offers])
        if fuzzy_destination is None:
            print("Nu s-a gasit nicio destinatie similara.")
            return
        if destination != fuzzy_destination:
            print(f"ai vrut sa spui {fuzzy_destination}")
            valid = input("Da sau Nu?  => ")
            if valid[0].lower() != "d":
                return
        prices = [offer.price for offer in self.__offers if offer.destination == fuzzy_destination]
        if not prices:
            print(f"Nu exista oferte pentru destinatia {destination}.")
        else:
            avg_price = sum(prices) / len(prices)
            print(f"Pretul mediu pentru destinatia {destination} este {avg_price:.2f} Euro.")

    def filter_by_month(self):
        print("\033[33mCautare pachete fara o anumita luna\033[0m")
        month = int(input("Introduceti luna: "))
        if month < 1 or month > 12:
            print("Luna invalida.")
            return
        
        selected_offers = [offer for offer in self.__offers if offer.start_date.month != month and offer.end_date.month != month]
        if not selected_offers:
            print(f"Nu există oferte pentru luna {month}.")
            return
        for offer in selected_offers:
            print(offer)

    def menu_handler(self, menu_id: int):
        while self.__running:
            print(self.meniu[menu_id])
            try:
                option = int(input("Alegeti o optiune: "))

                if menu_id == 0:
                    if option == 6:
                        self.handle_undo()
                    elif 1 <= option <= 5:
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

    def run(self):
        self.__running = True
        os.system("cls")
        self.menu_handler(0)

