
import difflib


def fuzzy_search_destination(query: str, destinations: list) -> str:
    """
    Caută o destinație folosind căutare fuzzy.
    """
    matches = difflib.get_close_matches(query, destinations, n=1, cutoff=0.4)
    if matches:
        return matches[0]
    else:
        return None



def validare_data(ziua,luna,anul):
    ziua = int(input("Ziua: "))
    if ziua < 1 or ziua > 31:
       raise ValueError("Ziua invalida")
    luna = int(input("Luna: "))
    if luna < 1 or luna > 12:
     raise ValueError("Luna invalida")
    anul = int(input("Anul: "))
    if anul < 1:
     raise ValueError("Anul invalid")
 
