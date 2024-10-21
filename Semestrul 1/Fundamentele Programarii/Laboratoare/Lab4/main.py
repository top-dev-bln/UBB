from offer import Package
import os
from datetime import datetime , timedelta
import difflib



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
        self.__history = []
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
        
    def test(self):
        self.add(datetime(2024, 6, 16), datetime(2024, 6, 20), "Craiova", 100)
        self.add(datetime(2024, 7, 2), datetime(2024, 7, 12), "Timisoara", 87)
        assert self.fuzzy_search_destination("Timisoara") == "Timisoara"
        self.handle_undo()
        assert self.fuzzy_search_destination("Timisoara") == None
        self.add(datetime(2024, 5, 12), datetime(2024, 8, 12), "Cluj-Napoca", 420)
        self.add(datetime(2024, 5, 4), datetime(2024, 8, 12), "Grecia, Athena", 69)
        self.add(datetime(2024, 5, 12), datetime(2024, 9, 12), "Craiova", 69)
        self.add(datetime(2024, 5, 12), datetime(2024, 8, 12), "Grecia, Athena", 420)
        self.add(datetime(2022, 2, 4), datetime(2024,3, 11), "barlad", 70)


        #testare fuzzy search
        assert self.fuzzy_search_destination("Craiova") == "Craiova"
        assert self.fuzzy_search_destination("Cluj") == "Cluj-Napoca"
        assert self.fuzzy_search_destination("Iasi") == None

    def __record_change(self, change_type, packages, previous=None):
        """
        Înregistrează o schimbare în history. Pentru modificări, stocam atât starea anterioară, cât și starea nouă.
        """
        self.__history.append({
            'type': change_type,
            'packages': packages,
            'previous': previous,  # Numai pentru modificari
        })

    def fuzzy_search_destination(self, query:str)->str:
         """
         Caută o destinație folosind căutare fuzzy.
         """
         destinations = [offer.destination for offer in self.__offers]
         
         matches = difflib.get_close_matches(query, destinations, n=1, cutoff=0.4)
         if matches:
             return matches[0]
         else:
             return None



            
    def handle_undo(self):
        """
        Reconstruiește lista inversând ultima operație.
        """
        if not self.__history:
            print("\033[31mNu se poate realiza undo. Nu există o stare anterioară disponibilă.\033[0m")
            return

        last_change = self.__history.pop()  # Get the last change
        change_type = last_change['type']

        if change_type == 'add':
            self.__offers.remove(last_change['packages'][0])
        elif change_type == 'delete':
            for package in last_change['packages']:
                self.__offers.append(package)
            print(f"Restored {len(last_change['packages'])} package(s)")
        elif change_type == 'modify':
            # Revert to the previous version of the package
            index = self.__offers.index(last_change['packages'][0])
            self.__offers[index] = last_change['previous']

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

    # Adaugare
    def add(self, start, end, destination, price):
        """
        Adauga un nou pachet si înregistrează modificările 
        """
        new_package = Package(start, end, destination, price)
        self.__offers.append(new_package)
        self.__record_change('add', new_package)


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
        self.add(data[0],data[1],destination,price)
        print("\033[32mPachet adaugat cu succes\033[0m") 
        print(str(self.__offers[-1]))

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
        new_data = self.get_date()
        destination = input("Destinatie: ")
        price = float(input("Pret: "))
        new_package = Package(new_data[0], new_data[1], destination, price)
        self.__offers[id] = new_package
        self.__record_change('modify', new_package, previous_package)
        print("\033[32mPachet modificat cu succes\033[0m")


    # Stergere
    def delete_by_destination(self)->None:
        """
        Sterge ofertele cu o destinație dată.
        """
        destination = input("Introduceți destinația de șters: ")
        fuzzy_destination = self.fuzzy_search_destination(destination)
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
            self.__offers = [offer for offer in self.__offers if offer.destination != fuzzy_destination]
            print(f"Am șters {len(removed_offers)} oferte cu destinația {fuzzy_destination}.")
        else:
            print(f"Nu există oferte cu destinația {fuzzy_destination}.")



    
    def delete_by_duration(self)->None:
        """
        Sterge ofertele care sunt sub  un anumit interval de timp.
        """
        duration = int(input("Introduceți durata de timp ( in zile ):  => "))
        if duration < 1:
            print("Durata invalidă")
            return
        
        removed_offers = [offer for offer in self.__offers if offer.end_date - offer.start_date > timedelta(days=duration)]
        if removed_offers:
            for offer in removed_offers:
                self.__offers.remove(offer)
                self.__record_change('delete', offer)
            self.__offers = [offer for offer in self.__offers if offer.end_date - offer.start_date <= timedelta(days=duration)]
            print(f"Ofertele cu durata de timp mai mică sau egală cu {duration} zile au fost șterse.")
        else:
            print(f"Nu există oferte cu durata de timp mai mică sau egală cu {duration} zile.")


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

        removed_offers = [offer for offer in self.__offers if offer.price > price]
        if removed_offers:
            for offer in removed_offers:
                self.__offers.remove(offer)
                self.__record_change('delete', offer)
            self.__offers = [offer for offer in self.__offers if offer.price <= price]
            print(f"Ofertele cu prețul mai mare de {price} Euro au fost șterse.")
        else:
            print(f"Nu există oferte cu prețul mai mare de {price} Euro.")

        


    # Cautare
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


        max_price = float(input("Introduceti pretul maxim: "))
        destination = input("Introduceți destinația: ")
        fuzzy_destination = self.fuzzy_search_destination(destination)
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
            if offer.destination == fuzzy_destination and offer.price <= max_price:
                print(offer)
                gasit = True
        if not gasit:
            print(f"Nu exista pachete cu destinatia {fuzzy_destination} si pretul mai mic sau egal cu {max_price}.")

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
            if offer.end_date == end_date:
                print(offer)
                gasit = True
        if not gasit:
            print(f"Nu exista pachete cu data de sfarsit inainte de {end_date.strftime('%Y-%m-%d')}.")

    # Report
    def report_offer_count(self):
        """
        Afiseaza numarul de oferte pentru o destinatie data.
        """
        print("\033[33mAfisare numar de oferte pentru o destinatie\033[0m")
        destination = input("Introduceti o destinatie: ")
        fuzzy_destination = self.fuzzy_search_destination(destination)
        if fuzzy_destination is None:
            print("Nu s-a gasit nicio destinatie similara.")
            return
        if destination != fuzzy_destination:
            print(f"ai vrut sa spui {fuzzy_destination}")
            valid = input("Da sau Nu?  => ")
            if valid[0].lower() != "d":
                return 
        count = 0
        for offer in self.__offers:
            if offer.destination == fuzzy_destination:
                count += 1
        if count == 0:
            print(f"Nu exista oferte pentru destinatia {fuzzy_destination}.")
        else:
            print(f"Exista {count} oferte pentru destinatia {fuzzy_destination}.")

    def report_packages_in_interval(self):
        """
        Afiseaza toate pachetele disponibile intr-un interval de timp dat, sortate crescator dupa pret.
        """
        print("\033[33mAfisare pachete disponibile intr-un interval de timp\033[0m")
        data = self.get_date()
        filtered_offers = [offer for offer in self.__offers if data[0] <= offer.start_date <= data[1]]
        

        if not filtered_offers:
            print(
                f"Nu exista pachete in intervalul {data[0].strftime('%Y-%m-%d')} - {data[1].strftime('%Y-%m-%d')}."
            )
        else:
            filtered_offers.sort(key=lambda offer: offer.price)
            for offer in filtered_offers:
                print(offer)

    def report_avg_price(self):
        """
        Afiseaza pretul mediu pentru o destinatie data.
        """
        print("\033[33mAfisare pret mediu pentru o destinatie\033[0m")
        destination = input("Introduceti destinatia: ")
        fuzzy_destination = self.fuzzy_search_destination(destination)
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

    # Filter
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

    def run(self)->None:
        """
        Pornește bucla principală a aplicației.
        
        Curăță consola, setează semnalizatorul de rulare la True și apoi apelează gestionarul de meniu pentru a afișa meniul principal.
        """
        self.test()
        os.system("cls")
        self.__running = True
        self.menu_handler(0)  



if __name__ == "__main__":
    process = package_processor()
    process.run()
