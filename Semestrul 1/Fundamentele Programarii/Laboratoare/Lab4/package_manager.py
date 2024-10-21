from package import Package
from utils import get_date, fuzzy_search_destination
from datetime import datetime, timedelta

class PackageManager:
    def __init__(self):
        self.__offers = []
        self.__history = []

    def __record_change(self, change_type, packages, previous=None):
        """
        Înregistrează o schimbare în history. Pentru modificări, stocam atât starea anterioară, cât și starea nouă.
        """
        self.__history.append({
            'type': change_type,
            'packages': packages,
            'previous': previous,  # Numai pentru modificari
        })

    def handle_undo(self):
        """
        Reconstruiește lista inversând ultima operație.
        """
        if not self.__history:
            print("\033[31mNu se poate realiza undo. Nu există o stare anterioară disponibilă.\033[0m")
            return

        last_change = self.__history.pop() 
        change_type = last_change['type']

        if change_type == 'add':
            self.__offers.remove(last_change['packages'])
        elif change_type == 'delete':
            if isinstance(last_change['packages'], list):
                for package in last_change['packages']:
                    self.__offers.append(package)
                print(f"Restored {len(last_change['packages'])} package(s)")
            else:
                self.__offers.append(last_change['packages'])
                print("Restored 1 package")
        elif change_type == 'modify':
            # Revert to the previous version of the package
            index = self.__offers.index(last_change['packages'])
            self.__offers[index] = last_change['previous']

        print("\033[32mUndo realizat cu succes\033[0m")

    def add(self, start, end, destination, price):
        """
        Adauga un nou pachet si înregistrează modificările 
        """
        new_package = Package(start, end, destination, price)
        self.__offers.append(new_package)
        self.__record_change('add', new_package)

    def add_package(self):
        """
        Adaugă o ofertă nouă în lista de oferte.
        """
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
        self.add(data[0], data[1], destination, price)
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
        new_data = get_date()
        destination = input("Destinatie: ")
        price = float(input("Pret: "))
        new_package = Package(new_data[0], new_data[1], destination, price)
        self.__offers[id] = new_package
        self.__record_change('modify', new_package, previous_package)
        print("\033[32mPachet modificat cu succes\033[0m")

    def delete_by_destination(self):
        """
        Sterge ofertele cu o destinație dată.
        """
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
        """
        Sterge ofertele care sunt sub  un anumit interval de timp.
        """
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
            self.__record_change('delete', removed_offers)
            self.__offers = [offer for offer in self.__offers if offer not in removed_offers]
            print(f"Ofertele cu prețul mai mare de {price} Euro au fost șterse.")
        else:
            print(f"Nu există oferte cu prețul mai mare de {price} Euro.")

    def search_by_interval(self):
        """
        Cauta pachete in functie de un interval de timp dat.
        """
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
        """
        Cauta pachete in functie de destinatie si pret maxim.
        """
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

    def report_offer_count(self):
        """
        Afiseaza numarul de oferte pentru o destinatie data.
        """
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
        """
        Afiseaza toate pachetele disponibile intr-un interval de timp dat, sortate crescator dupa pret.
        """
        print("\033[33mAfisare pachete disponibile intr-un interval de timp\033[0m")
        data = get_date()
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
        """
        Eliminarea ofertelor în care sejurul presupune zile dintr-o anumită lună
        """
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

    def get_offers(self):
        return self.__offers
