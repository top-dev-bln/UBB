import os
from datetime import datetime, timedelta
from package import Package
from utils import fuzzy_search_destination
from console import get_date, meniu


class PackageManager:
    def __init__(self):

        self.__offers = []
        self.__history = []
        self.__running = False
        self.__submenu_functions = {
            1: {1: self.add_package, 2: self.modify_package, 3: self.handle_undo},  # Add Menu
            2: {1: self.delete_by_destination, 2: self.delete_by_duration, 3: self.delete_by_price, 4: self.handle_undo},  # Delete Menu
            3: {1: self.search_by_interval, 2: self.search_by_destination_price, 3: self.search_by_end_date},  # Search Menu
            4: {1: self.report_offer_count, 2: self.report_packages_in_interval, 3: self.report_avg_price},  # Report Menu
            5: {1: self.search_by_destination_price, 2: self.filter_by_month},  # Filter Menu
        }

   
    def get_offers(self):
        """
        Returnează lista de oferte disponibile.

        Returns:
            list: O listă conținând toate ofertele curente.
        """
        return self.__offers

    def __record_change(self, change_type:str, packages:list, previous:Package=None):
        """
        Înregistrează o modificare în istoricul aplicației.

        Args:
            change_type (str): Tipul modificării ('add', 'delete', 'modify').
            packages (list): Lista de pachete afectate de modificare.
            previous (Package, optional): Pachetul anterior în cazul unei modificări. Implicit None.
        """
        self.__history.append({
            'type': change_type,
            'packages': packages,
            'previous': previous,
        })

    def handle_undo(self):
        """
        Anulează ultima acțiune efectuată și restaurează starea anterioară a ofertelor.

        Această functie gestionează operațiunea de undo pentru diferite tipuri de modificări:
        - Pentru adăugări: elimină pachetul adăugat recent
        - Pentru ștergeri: restaurează pachetele șterse
        - Pentru modificări: înlocuiește pachetul modificat cu versiunea sa anterioară

        Dacă nu există nicio acțiune anterioară în istoric, se afișează un mesaj corespunzător.

        Returnează:
            None
        """
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

    def add_package_api(self, start_date:datetime, end_date:datetime, destination:str, price:float):
        """
        Adaugă un nou pachet de vacanță în lista de oferte.

        Args:
            start_date (datetime): Data de început a pachetului.
            end_date (datetime): Data de sfârșit a pachetului.
            destination (str): Destinația pachetului.
            price (float): Prețul pachetului.

        Returns:
            Package: Obiectul pachet nou creat și adăugat în listă.
        """
        new_package = Package(start_date, end_date, destination, price)
        self.__offers.append(new_package)
        self.__record_change('add', [new_package])
        return new_package

    def add_package(self):
        """
        Obține datele necesare pentru crearea unui nou pachet de vacanță și îl adaugă în sistem.

        Această funcție solicită utilizatorului să introducă:
        - Data de început și de sfârșit a pachetului
        - Destinația
        - Prețul
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
        package = self.add_package_api(data[0], data[1], destination, price)
        print("\033[32mPachet adaugat cu succes\033[0m")
        print(str(package))

    def modify_package_api(self, id:int, start_date:datetime, end_date:datetime, destination:str, price:float):
        """
        Modifică un pachet existent în lista de oferte.

        Args:
            id (int): Indexul pachetului în lista de oferte.
            start_date (datetime): Noua dată de început a pachetului.
            end_date (datetime): Noua dată de sfârșit a pachetului.
            destination (str): Noua destinație a pachetului.
            price (float): Noul preț al pachetului.
        Returns:
            bool: True dacă modificarea a fost realizată cu succes
        """
        previous_package = self.__offers[id]
        new_package = Package(start_date, end_date, destination, price)
        self.__offers[id] = new_package
        self.__record_change('modify', [new_package], previous_package)
        return True

    def modify_package(self):
        """
        Modifică un pachet existent în lista de oferte.

        Această funcție permite utilizatorului să selecteze un pachet din lista de oferte
        și să îi modifice detaliile (data de început, data de sfârșit, destinația și prețul).
        Dacă nu există pachete disponibile, se afișează un mesaj corespunzător.
        
        Returns:
            None
        """
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
        
        new_data = get_date()
        destination = input("Destinatie: ")
        while True:
            try:
                price = float(input("Pret: "))
                if price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Pret invalid. Va rugam introduceti un numar pozitiv.")
        
        if self.modify_package_api(id, new_data[0], new_data[1], destination, price):
            print("\033[32mPachet modificat cu succes\033[0m")
        else:
            print("\033[31mModificarea pachetului a esuat\033[0m")


    
    def delete_api(self, condition):
        """
        Șterge ofertele care îndeplinesc o anumită condiție.

        Args:
            condition (functie): O funcție care primește o ofertă și returnează True dacă oferta trebuie ștearsă.

        Returns:
            int: Numărul de oferte șterse.

        Această metodă parcurge lista de oferte, identifică ofertele care îndeplinesc condiția specificată,
        le înregistrează în istoric și le elimină din lista de oferte active.
        """
        removed_offers = [offer for offer in self.__offers if condition(offer)]
        self.__record_change('delete', removed_offers)
        self.__offers = [offer for offer in self.__offers if not condition(offer)]
        return len(removed_offers)

    def delete_by_destination(self):
        """
        Șterge ofertele pentru o destinație specificată de utilizator.

        Această metodă permite utilizatorului să introducă o destinație și folosește
        căutarea fuzzy pentru a identifica destinația corectă. Apoi, șterge toate
        ofertele care au acea destinație.

        Nu are parametri și nu returnează nimic.
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
                os.system("cls")
                return
        
        len = self.delete_api(lambda offer: offer.destination == fuzzy_destination)
        
        if len:
            print(f"Am șters {len} oferte cu destinația {fuzzy_destination}.")
        else:
            print(f"Nu există oferte cu destinația {fuzzy_destination}.")

    def delete_by_duration(self):
        """
        Șterge ofertele cu o durată mai scurta decât cea specificată de utilizator.

        Returnează:
            None
        """
        duration = int(input("Introduceți durata de timp ( in zile ):  => "))
        if duration < 1:
            print("Durata invalidă")
            return
        
        len = self.delete_api(lambda offer: offer.end_date-offer.start_date<timedelta(days=duration))
        
        if len:
            print(f"{len} oferte cu durata de timp mai mica decât {duration} zile au fost șterse.")
        else:
            print(f"Nu există oferte cu durata de timp mai mica decât {duration} zile.")
    
    def delete_by_price(self):
        """
        Șterge ofertele cu un preț mai mare decât cel specificat de utilizator.

        Nu primește parametri și nu returnează nimic.
        """
        while True:
            try:
                price = float(input("Introduceți prețul maxim: "))
                if price < 0:
                    raise ValueError
                break
            except ValueError:
                print("Preț invalid. Va rugam introduceti un numar pozitiv.")

        len = self.delete_api(lambda offer: offer.price > price)
        if len:
            print(f"{len} oferte cu prețul mai mare de {price} Euro au fost șterse.")
        else:
            print(f"Nu există oferte cu prețul mai mare de {price} Euro.")

    def search_by_interval_api(self, data:tuple):
        """
        Caută pachete de vacanță în funcție de un interval de timp dat.

        Args:
            data (tuple): Un tuplu conținând data de început și data de sfârșit a intervalului.

        Returns:
            list: O listă cu toate ofertele care se încadrează în intervalul de timp specificat.
        """
        return [offer for offer in self.__offers if data[0] <= offer.start_date and data[1] >= offer.end_date]

    def search_by_interval(self):
        """
        Caută și afișează pachetele de vacanță disponibile într-un interval de timp specificat.

        Dacă sunt găsite pachete în intervalul specificat, acestea sunt afișate individual.
        Dacă nu sunt găsite pachete, se afișează un mesaj corespunzător.

        Nu are parametri și nu returnează nimic.
        """
        print("\033[33mCautare pachete in functie de un interval de timp dat\033[0m")
        data = get_date()

        results = self.search_by_interval_api(data)
        
        if results!=[]:
            for offer in results:
                print(str(offer))
        
        else:
            print(f"Nu exista pachete in intervalul {data[0].strftime('%Y-%m-%d')} - {data[1].strftime('%Y-%m-%d')}.")

    def search_by_destination_price_api(self, destination: str, max_price: float):
        """
        Caută pachete de vacanță în funcție de destinație și preț maxim.

        Args:
            destination (str): Destinația căutată.
            max_price (float): Prețul maxim acceptat.

        Returns:
            list: O listă cu toate ofertele care corespund criteriilor de căutare.
        """
        return [offer for offer in self.__offers if offer.destination == destination and offer.price < max_price]
    
    def search_by_destination_price(self):
        """
        Caută și afișează pachete de vacanță în funcție de destinație și preț maxim.

        Nu are parametri și nu returnează nimic.
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
        
        results = self.search_by_destination_price_api(fuzzy_destination, max_price)
        if results!=[]:
            for offer in results:
                print(offer)
        else:
            print(f"Nu exista pachete cu destinatia {fuzzy_destination} si pretul mai mic sau egal cu {max_price}.")

    def search_by_end_date_api(self, end_date: datetime):
        """
        Caută pachete de vacanță în funcție de data de sfârșit.

        Args:
            end_date (datetime): Data de sfârșit a căutării.

        Returns:
            list: O listă cu toate ofertele care corespund criteriilor de căutare.
        """
        return [offer for offer in self.__offers if offer.end_date == end_date]

    def search_by_end_date(self):
        """
        Caută și afișează pachete de vacanță în funcție de data de sfârșit.
        
        Nu are parametri și nu returnează nimic.

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
        results = self.search_by_end_date_api(end_date)
        if results!=[]:
            for offer in results:
                print(offer)
        else:
            print(f"Nu exista pachete cu data de sfarsit inainte de {end_date.strftime('%Y-%m-%d')}.")

    def report_offer_count_api(self, destination: str):
        """
        Numără ofertele pentru o destinație specifică.

        Args:
            destination (str): Destinația pentru care se numără ofertele.

        Returns:
            int: Numărul de oferte pentru destinația specificată.
        """
        return len([offer for offer in self.__offers if offer.destination == destination])

    def report_offer_count(self):
        """
        Afișează numărul de oferte pentru o destinație specificată de utilizator.

        Nu are parametri și nu returnează nimic.
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
        count = self.report_offer_count_api(fuzzy_destination)
        if count:
            print(f"Exista {count} oferte pentru destinatia {fuzzy_destination}.")
        else:
            print(f"Nu exista oferte pentru destinatia {fuzzy_destination}.")

    def report_packages_in_interval_api(self,data:tuple): 
        """
        Afișează pachetele disponibile într-un interval de timp specificat sortate după preț.
        
        Args:
            data (tuple): Un tuple conținând data de început și data de sfârșit a intervalului.

        Returns:
            list: O listă cu toate pachetele disponibile într-un interval de timp specificat și sortate după preț.
        """
        offers =[offer for offer in self.__offers if data[0] <= offer.start_date and data[1] >= offer.end_date]
        offers.sort(key=lambda offer: offer.price)
        return offers

    def report_packages_in_interval(self):
        """
        Raportează și afișează pachetele de vacanță disponibile într-un interval de timp specificat.

        Functia nu primește parametri și nu returnează nimic.
        """
        data = get_date()
        filtered_offers = self.report_packages_in_interval_api(data)
        
        if filtered_offers!=[]:
            for offer in filtered_offers:
                print(offer)
        else:
            print(f"Nu exista pachete in intervalul {data[0].strftime('%Y-%m-%d')} - {data[1].strftime('%Y-%m-%d')}.")

    def report_avg_price_api(self, destination: str):
        """
        Afișează pretul mediu pentru o destinație specificată.

        Args:
            destination (str): Destinația pentru care se afișează pretul mediu.

        Returns:
            float: Pretul mediu pentru destinația specificată.
        """
        offers = [offer.price for offer in self.__offers if offer.destination == destination]
        if offers:
            return sum(offers) / len(offers)
        return 0
    
    def report_avg_price(self):
        """
        Afișează prețul mediu pentru o destinație specificată de utilizator.

        Nu are parametri și nu returnează nimic.
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
        avg_price = self.report_avg_price_api(fuzzy_destination)
        print(f"Pretul mediu pentru destinatia {destination} este {avg_price:.2f} Euro.")

    def filter_by_month_api(self, month: int):
        """
        Filtrează ofertele care nu au loc în luna specificată

        Args:
            month (int): Luna pentru care se face filtrarea (se așteaptă un număr de la 1 la 12).

        Returns:
            list: O listă de oferte care nu au loc în luna specificată.
        """
        return [offer for offer in self.__offers if not (
            (offer.start_date.month <= month <= offer.end_date.month) or
            (offer.start_date.month > offer.end_date.month and (month >= offer.start_date.month or month <= offer.end_date.month))
        )]

    def filter_by_month(self):
        """
        Filtrează și afișează pachetele de vacanță care nu au loc într-o anumită lună.

        Nu are parametri și nu returnează nimic.
        """
        print("\033[33mCautare pachete fara o anumita luna\033[0m")
        month = int(input("Introduceti luna: "))
        if month < 1 or month > 12:
            print("Luna invalida.")
            return
        
        selected_offers = self.filter_by_month_api(month)
        if not selected_offers:
            print(f"Nu există oferte pentru luna {month}.")
            return
        for offer in selected_offers:
            print(offer)
 
    def menu_handler(self, menu_id: int=0):
        """
        Se ocupă de navigarea prin meniuri

        Această metodă afișează meniul bazat pe menu_id execută acțiunile corespunzătoare.
        Metoda rulează în buclă până când utilizatorul alege să iasă sau revine la un meniu anterior.

        Argumente:
            menu_id (int): ID-ul meniului curent de afișat.
                           0 reprezintă meniul principal, alte valori
                           reprezintă submeniuri.
        """
        while self.__running:
            print(meniu[menu_id])
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
        """
        Pornește și rulează aplicația de gestionare a pachetelor de vacanță.
        Această functie inițializează starea de rulare a aplicației și apeleaza menu_hadler.

        Nu primește parametri și nu returnează nicio valoare.
        """
        os.system("cls")
        self.__running = True
        self.menu_handler()