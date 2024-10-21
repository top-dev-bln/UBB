from datetime import datetime
import difflib

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

def fuzzy_search_destination(query: str, destinations: list) -> str:
    """
    Caută o destinație folosind căutare fuzzy.
    """
    matches = difflib.get_close_matches(query, destinations, n=1, cutoff=0.4)
    if matches:
        return matches[0]
    else:
        return None

def test_fuzzy_search():
    destinations = ["Paris", "London", "New York", "Tokyo", "Sydney"]

    assert fuzzy_search_destination("Paris", destinations) == "Paris"
    assert fuzzy_search_destination("Pari", destinations) == "Paris"
    assert fuzzy_search_destination("london", destinations) == "London"
    assert fuzzy_search_destination("Berlin", destinations) is None
    assert fuzzy_search_destination("", destinations) is None
    assert fuzzy_search_destination("Paris", []) is None


test_fuzzy_search()

