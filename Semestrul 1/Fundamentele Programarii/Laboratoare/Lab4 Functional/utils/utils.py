
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



def dict2string(offer: dict):
    """
    Convertește un dicționar care reprezintă o ofertă de călătorie într-un șir formatat.

    Argumente:
        offer (dict): Un dicționar care conține detaliile ofertei de călătorie.
                      Cheile așteptate sunt 'destination', 'start_date', 'end_date' și 'price'.
                      'start_date' și 'end_date' ar trebui să fie obiecte datetime.

    Returnează:
        str: Un șir formatat care descrie oferta de călătorie.
    """  
    return (f"{offer['destination']} ({offer['start_date'].strftime('%Y-%m-%d')} - {offer['end_date'].strftime('%Y-%m-%d')}): {offer['price']} Euro")


