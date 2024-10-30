from datetime import datetime, timedelta
from domain.package_manager import *
from utils.utils import fuzzy_search_destination, dict2string
from domain.validare import validare_data, validare_pret
import os

meniu = {
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


def handle_undo(manager):
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
   
    if not manager["history"]:
        print("\033[31mNu se poate realiza undo. Nu există o stare anterioară disponibilă.\033[0m")
        return
    undo_api(manager)
    print("\033[32mUndo realizat cu succes\033[0m")





def get_date():


    """
    Obține de la utilizator datele de început și de sfârșit ale unei perioade, asigurându-se că sunt valide și că data de început este înaintea datei de sfârșit.
    Returns:
        list: O listă care conține două obiecte datetime, reprezentând data de început și data de sfârșit.
    """
    os.system("cls")
    data = []
    labels = ["inceput", "sfarsit"]
    while True:
        for label in labels:
            while True:
                try:
                    print(f"Introduceti data de {label}")
                    ziua = int(input("Ziua: "))
                    luna = int(input("Luna: "))
                    anul = int(input("Anul: "))
                    validare_data(ziua,luna,anul)
                    data.append(datetime(anul, luna, ziua))
                    break
                except ValueError as e:
                    print(f"\033[31m{e}\033[0m")


        if data[0] > data[1]:
            print("Data de inceput trebuie sa fie inaintea data de sfarsit")
            data.pop()
            data.pop()
            continue
        else:
            return data
        
def citire_info():
    """
    Citeste informatii de la utilizator.
    Functia citeste data, destinatia si pretul de la utilizator. 
    Pretul este validat pentru a fi un numar pozitiv.
    Returns:
            data de inceput:datetime, data de sfarsit:datetime, destinatia:str , pretul:float
    """
    data = get_date()
    destination = input("Introduceti destinatia: ")
    while True:
        try:
            price = float(input("Introduceti pretul: "))
            validare_pret(price)
            break
        except ValueError:
            print("Pret invalid. Va rugam introduceti un numar pozitiv.")

    return data[0],data[1],destination, price


def estimare_destinatie(manager, destination:str):
    offers = manager["offers"]
    fuzzy_destination = fuzzy_search_destination(destination, [offer["destination"] for offer in offers])
    if fuzzy_destination is None:
        print("Nu s-a gasit nicio destinatie similara.")
        return
    if destination != fuzzy_destination:
      print(f"ai vrut sa spui {fuzzy_destination}")
    valid = input("Da sau Nu?  => ")
    if valid[0].lower() != "d":
        return 
    return fuzzy_destination

def add_package(manager):
    """
    Obține datele necesare pentru crearea unui nou pachet de vacanță și îl adaugă în sistem.

    Această funcție solicită utilizatorului să introducă:
    - Data de început și de sfârșit a pachetului
    - Destinația
    - Prețul
    """
    
    start, end, destination, price = citire_info()
    package = add_package_api(manager, start, end, destination, price)
    print("\033[32mPachet adaugat cu succes\033[0m")
    print(dict2string(package))


def print_offers(offers:list):
    """
    Afișează o listă de oferte.

    Parametri:
    offers (list): Lista de oferte care trebuie afișate. Fiecare ofertă este un dicționar.

    Returnează:
    None
    """
    for i, offer in enumerate(offers):
        print(f"{i+1}. " + dict2string(offer))



def modify_package(manager):
    """
    Modifică un pachet existent în lista de oferte.

    Această funcție permite utilizatorului să selecteze un pachet din lista de oferte
    și să îi modifice detaliile (data de început, data de sfârșit, destinația și prețul).
    Dacă nu există pachete disponibile, se afișează un mesaj corespunzător.
    
    Returns:
        None
    """
    print("\033[33mModificare pachet\033[0m")
    if not manager["offers"]:
        print("Nu exista pachete disponibile pentru modificare.")
        return
    print("Ce pachet doriti sa modificati?")
        
    print_offers(manager["offers"])
    id = int(input("=> ")) - 1


    #citire id
    if id < 0 or id >= len(manager["offers"]):
        print("Id-ul introdus este invalid.")
        return
    
    new_start, new_end, destination, price = citire_info()
    
    if modify_package_api(manager, id, new_start, new_end, destination, price):
        print("\033[32mPachet modificat cu succes\033[0m")
    else:
        print("\033[31mModificarea pachetului a esuat\033[0m")


def delete_by_destination(manager):
    """
    Șterge ofertele pentru o destinație specificată de utilizator.

    Această metodă permite utilizatorului să introducă o destinație și folosește
    căutarea fuzzy pentru a identifica destinația corectă. Apoi, șterge toate
    ofertele care au acea destinație.

    Nu are parametri și nu returnează nimic.
    """
  
    destination = input("Introduceți destinația de șters: ")
    fuzzy_destination = estimare_destinatie(manager, destination)
    if fuzzy_destination == None:
        return
    print(fuzzy_destination)
    len = delete_api(manager,lambda offer: offer["destination"] == fuzzy_destination)
    
    if len:
        print(f"Am șters {len} oferte cu destinația {fuzzy_destination}.")
    else:
        print(f"Nu există oferte cu destinația {fuzzy_destination}.")


def delete_by_duration(manager):
    """
    Șterge ofertele cu o durată mai scurta decât cea specificată de utilizator.

    Returnează:
        None
    """
    duration = int(input("Introduceți durata de timp ( in zile ):  => "))
    if duration < 1:
        print("Durata invalidă")
        return
    
    len = delete_api(manager,lambda offer: offer["end_date"]-offer["start_date"]<timedelta(days=duration))
    
    if len:
        print(f"{len} oferte cu durata de timp mai mica decât {duration} zile au fost șterse.")
    else:
        print(f"Nu există oferte cu durata de timp mai mica decât {duration} zile.")


def delete_by_price(manager):
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

    len = delete_api(manager,lambda offer: offer["price"] > price)
    if len:
        print(f"{len} oferte cu prețul mai mare de {price} Euro au fost șterse.")
    else:
        print(f"Nu există oferte cu prețul mai mare de {price} Euro.")


def search_by_interval(manager):
    """
    Caută și afișează pachetele de vacanță disponibile într-un interval de timp specificat.

    Dacă sunt găsite pachete în intervalul specificat, acestea sunt afișate individual.
    Dacă nu sunt găsite pachete, se afișează un mesaj corespunzător.

    Nu are parametri și nu returnează nimic.
    """
    print("\033[33mCautare pachete in functie de un interval de timp dat\033[0m")
    data = get_date()

    results = search_by_interval_api(manager,data)
    
    if results!=[]:
        print_offers(results)

    else:
        print(f"Nu exista pachete in intervalul {data[0].strftime('%Y-%m-%d')} - {data[1].strftime('%Y-%m-%d')}.")


def search_by_destination_price(manager):
    """
    Caută și afișează pachete de vacanță în funcție de destinație și preț maxim.

    Nu are parametri și nu returnează nimic.
    """
    print("\033[33mCautare pachete in functie de destinatie si pret maxim\033[0m")

    max_price = float(input("Introduceti pretul maxim: "))
    destination = input("Introduceți destinația: ")
    
    fuzzy_destination = estimare_destinatie(manager, destination)
    if fuzzy_destination == None:
        return
    
    
    results = search_by_destination_price_api(manager,fuzzy_destination, max_price)
    if results!=[]:
        print_offers(results)
    else:
        print(f"Nu exista pachete cu destinatia {fuzzy_destination} si pretul mai mic sau egal cu {max_price}.")


def search_by_end_date(manager):
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
    results = search_by_end_date_api(manager,end_date)
    if results!=[]:
        print_offers(results)

    else:
        print(f"Nu exista pachete cu data de sfarsit inainte de {end_date.strftime('%Y-%m-%d')}.")


def report_offer_count(manager):
    """
    Afișează numărul de oferte pentru o destinație specificată de utilizator.

    Nu are parametri și nu returnează nimic.
    """
    print("\033[33mAfisare numar de oferte pentru o destinatie\033[0m")
    destination = input("Introduceti o destinatie: ")
    fuzzy_destination = estimare_destinatie(manager, destination)
    if fuzzy_destination == None:
        return
    
    count = report_offer_count_api(manager,fuzzy_destination)
    if count:
        print(f"Exista {count} oferte pentru destinatia {fuzzy_destination}.")
    else:
        print(f"Nu exista oferte pentru destinatia {fuzzy_destination}.")


def report_packages_in_interval(manager):
    """
    Raportează și afișează pachetele de vacanță disponibile într-un interval de timp specificat.

    Functia nu primește parametri și nu returnează nimic.
    """
    data = get_date()
    filtered_offers = report_packages_in_interval_api(manager,data)
    
    if filtered_offers!=[]:
        print_offers(filtered_offers)
    else:
        print(f"Nu exista pachete in intervalul {data[0].strftime('%Y-%m-%d')} - {data[1].strftime('%Y-%m-%d')}.")


def report_avg_price(manager):
    """
    Afișează prețul mediu pentru o destinație specificată de utilizator.

    Nu are parametri și nu returnează nimic.
    """
    print("\033[33mAfisare pret mediu pentru o destinatie\033[0m")
    destination = input("Introduceti destinatia: ")
 
    fuzzy_destination = estimare_destinatie(manager, destination)
    if fuzzy_destination == None:
        return
    
    avg_price = report_avg_price_api(manager,fuzzy_destination)
    print(f"Pretul mediu pentru destinatia {destination} este {avg_price:.2f} Euro.")


def filter_by_month(manager):
    """
    Filtrează și afișează pachetele de vacanță care nu au loc într-o anumită lună.

    Nu are parametri și nu returnează nimic.
    """
    print("\033[33mCautare pachete fara o anumita luna\033[0m")
    month = int(input("Introduceti luna: "))
    if month < 1 or month > 12:
        print("Luna invalida.")
        return
    
    selected_offers = filter_by_month_api(manager,month)
    if not selected_offers:
        print(f"Nu există oferte pentru luna {month}.")
        return
    print_offers(selected_offers)


submenu_functions = {
    1: {1: add_package, 2: modify_package, 3:handle_undo},  # Add Menu
    2: {1: delete_by_destination, 2: delete_by_duration, 3: delete_by_price, 4:handle_undo},  # Delete Menu
    3: {1: search_by_interval, 2: search_by_destination_price, 3: search_by_end_date},  # Search Menu
    4: {1: report_offer_count, 2: report_packages_in_interval, 3: report_avg_price},  # Report Menu
    5: {1: search_by_destination_price, 2: filter_by_month},  # Filter Menu
}

def submenu(id,manager):
    """
    Afișează un submeniu și gestionează opțiunile selectate de utilizator.

    Parametri:
    id (int): Identificatorul submeniului care trebuie afișat.
    manager (object): Un obiect manager care gestionează funcțiile submeniului.
    """
    os.system("cls")
    while True:
        print(meniu[id])
        try:
            option = int(input("Introduceti optiunea: "))
            if option == 9:
                return
            elif option > 0 and option <= len(submenu_functions[id]):
                submenu_functions[id][option](manager)
        except ValueError:
            print("Introduceti un numar valid.")

def run():
    """
    Se ocupă de navigarea prin meniuri

    :params:
    nu are parametrii
    """
    manager=create_manager()
    while True:
        print(meniu[0])
        try:
            option = int(input("Introduceti optiunea: "))
            if option == 9:
                break
            elif option == 6:
                handle_undo(manager)
            elif option > 0 and option <= len(submenu_functions):
                submenu(option,manager)
        except ValueError:
            print("Introduceti un numar valid.")