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

import unittest

class TestFuzzySearch(unittest.TestCase):
    def setUp(self):
        self.destinations = ["Paris", "London", "New York", "Tokyo", "Sydney"]

    def test_exact_match(self):
        self.assertEqual(fuzzy_search_destination("Paris", self.destinations), "Paris")

    def test_close_match(self):
        self.assertEqual(fuzzy_search_destination("Pari", self.destinations), "Paris")

    def test_case_insensitive(self):
        self.assertEqual(fuzzy_search_destination("london", self.destinations), "London")

    def test_no_match(self):
        self.assertIsNone(fuzzy_search_destination("Berlin", self.destinations))

    def test_empty_query(self):
        self.assertIsNone(fuzzy_search_destination("", self.destinations))

    def test_empty_destinations(self):
        self.assertIsNone(fuzzy_search_destination("Paris", []))

if __name__ == '__main__':
    unittest.main()

