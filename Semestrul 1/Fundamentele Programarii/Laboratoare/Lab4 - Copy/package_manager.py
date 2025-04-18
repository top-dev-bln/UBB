
from datetime import datetime




class PackageManager:
    def __init__(self):

        self.__offers = []
        self.__history = []
        self.__running = True


    def is_running(self):
        """
        Verifică dacă aplicația este în curs de rulare.

        Returns:
            bool: True dacă aplicația este în curs de rulare, False în caz contrar.
        """
        return self.__running
    

   
    def get_offers(self):
        """
        Returnează lista de oferte disponibile.

        Returns:
            list: O listă conținând toate ofertele curente.
        """
        return self.__offers

    def get_history(self):
        """
        Returnează lista de oferte disponibile.

        Returns:
            list: O listă conținând toate ofertele curente.
        """
        return self.__history


    def undo_api(self):
        """
        Anulează ultima modificare efectuată în aplicație.

        Returns:
            None
        """
       
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

    def __record_change(self, change_type:str, packages:list, previous:dict=None):
        """
        Înregistrează o modificare în istoricul aplicației.

        Args:
            change_type (str): Tipul modificării ('add', 'delete', 'modify').
            packages (list): Lista de pachete afectate de modificare.
            previous (dict, optional): Pachetul anterior în cazul unei modificări. Implicit None.
        """
        self.__history.append({
            'type': change_type,
            'packages': packages,
            'previous': previous,
        })



    def add_package_api(self, start_date:datetime, end_date:datetime, destination:str, price:float):
        """
        Adaugă un nou pachet de vacanță în lista de oferte.

        Args:
            start_date (datetime): Data de început a pachetului.
            end_date (datetime): Data de sfârșit a pachetului.
            destination (str): Destinația pachetului.
            price (float): Prețul pachetului.

        Returns:
            Package: Dictionarul pachet nou creat și adăugat în listă.
        """
        

        new_package = {"start_date": start_date,
                       "end_date": end_date,
                       "destination": destination, 
                       "price": price}
        self.__offers.append(new_package)
        self.__record_change('add', [new_package])
        return new_package



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
        new_package = {"start_date": start_date,
                       "end_date": end_date,
                       "destination": destination, 
                       "price": price}
        self.__offers[id] = new_package
        self.__record_change('modify', [new_package], previous_package)
        return True




    
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



    def search_by_interval_api(self, data:tuple):
        """
        Caută pachete de vacanță în funcție de un interval de timp dat.

        Args:
            data (tuple): Un tuplu conținând data de început și data de sfârșit a intervalului.

        Returns:
            list: O listă cu toate ofertele care se încadrează în intervalul de timp specificat.
        """
        return [offer for offer in self.__offers if data[0] <= offer["start_date"] and data[1] >= offer["end_date"]]

    def search_by_destination_price_api(self, destination: str, max_price: float):
        """
        Caută pachete de vacanță în funcție de destinație și preț maxim.

        Args:
            destination (str): Destinația căutată.
            max_price (float): Prețul maxim acceptat.

        Returns:
            list: O listă cu toate ofertele care corespund criteriilor de căutare.
        """
        return [offer for offer in self.__offers if offer["destination"] == destination and offer["price"] < max_price]

    def search_by_end_date_api(self, end_date: datetime):
        """
        Caută pachete de vacanță în funcție de data de sfârșit.

        Args:
            end_date (datetime): Data de sfârșit a căutării.

        Returns:
            list: O listă cu toate ofertele care corespund criteriilor de căutare.
        """
        return [offer for offer in self.__offers if offer["end_date"] == end_date]


    def report_offer_count_api(self, destination: str):
        """
        Numără ofertele pentru o destinație specifică.

        Args:
            destination (str): Destinația pentru care se numără ofertele.

        Returns:
            int: Numărul de oferte pentru destinația specificată.
        """
        return len([offer for offer in self.__offers if offer["destination"] == destination])


    def report_packages_in_interval_api(self,data:tuple): 
        """
        Afișează pachetele disponibile într-un interval de timp specificat sortate după preț.
        
        Args:
            data (tuple): Un tuple conținând data de început și data de sfârșit a intervalului.

        Returns:
            list: O listă cu toate pachetele disponibile într-un interval de timp specificat și sortate după preț.
        """
        offers =[offer for offer in self.__offers if data[0] <= offer["start_date"] and data[1] >= offer["end_date"]]
        offers.sort(key=lambda offer: offer["price"])
        return offers


    def report_avg_price_api(self, destination: str):
        """
        Afișează pretul mediu pentru o destinație specificată.

        Args:
            destination (str): Destinația pentru care se afișează pretul mediu.

        Returns:
            float: Pretul mediu pentru destinația specificată.
        """
        offers = [offer["price"] for offer in self.__offers if offer["destination"] == destination]
        if offers:
            return sum(offers) / len(offers)
        return 0

    def filter_by_month_api(self, month: int):
        """
        Filtrează ofertele care nu au loc în luna specificată

        Args:
            month (int): Luna pentru care se face filtrarea (se așteaptă un număr de la 1 la 12).

        Returns:
            list: O listă de oferte care nu au loc în luna specificată.
        """
        return [offer for offer in self.__offers if not (
            (offer["start_date"].month <= month <= offer["end_date"].month) or
            (offer["start_date"].month > offer["end_date"].month and (month >= offer["start_date"].month or month <= offer["end_date"].month))
        )]


