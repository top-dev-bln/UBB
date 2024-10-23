
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



