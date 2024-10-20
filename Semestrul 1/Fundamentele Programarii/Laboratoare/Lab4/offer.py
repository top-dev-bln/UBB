from datetime import datetime

class Package:
    """
    Reprezintă un pachet turistic.
    """

    def __init__(self, start_date: datetime, end_date: datetime, destination: str, price: float) -> None:
        """
        Inițializează un obiect Package.

        Args:
            start_date (datetime): Data de început a pachetului.
            end_date (datetime): Data de sfârșit a pachetului.
            destination (str): Destinația pachetului.
            price (float): Prețul pachetului.
        """
        self.start_date = start_date
        self.end_date = end_date
        self.destination = destination
        self.price = price

    def get_destination(self) -> str:
        """
        Returnează destinația pachetului.

        Returns:
            str: Destinația pachetului.
        """
        return self.destination

    def __str__(self) -> str:
        """
        Returnează o reprezentare text a pachetului.

        Returns:
            str: Reprezentarea text a pachetului.
        """
        return f"Pachetul cu destinația {self.destination} are prețul {self.price} Euro și este disponibil între {self.start_date.strftime('%Y-%m-%d')} și {self.end_date.strftime('%Y-%m-%d')}"
