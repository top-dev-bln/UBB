from datetime import datetime


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


def get_date():
    """
    Obține de la utilizator datele de început și de sfârșit ale unei perioade, asigurându-se că sunt valide și că data de început este înaintea datei de sfârșit.
    Returns:
        list: O listă care conține două obiecte datetime, reprezentând data de început și data de sfârșit.
    """
    data = []
    labels = ["inceput", "sfarsit"]
    while True:
        for label in labels:
            while True:
                try:
                    print(f"Introduceti data de {label}")
                    ziua = int(input("Ziua: "))
                    if ziua < 1 or ziua > 31:
                        raise ValueError("Ziua invalida")
                    luna = int(input("Luna: "))
                    if luna < 1 or luna > 12:
                        raise ValueError("Luna invalida")
                    anul = int(input("Anul: "))
                    if anul < 1:
                        raise ValueError("Anul invalid")
                    data.append(datetime(anul, luna, ziua))
                    break
                except ValueError as e:
                    print(f"\033[31m{e}\033[0m")
        if data[0] > data[1]:
            print("Data de inceput trebuie sa fie inaintea data de sfarsit")
            data.pop()
            continue
        else:
            return data