from datetime import datetime

class Package:
    def __init__(self, start: datetime, end: datetime, destination: str, price: float):
        """
        Inițializează un obiect Package.

        Args:
            start_date (datetime): Data de început a pachetului.
            end_date (datetime): Data de sfârșit a pachetului.
            destination (str): Destinația pachetului.
            price (float): Prețul pachetului.
        """
        self.start_date = start
        self.end_date = end
        self.destination = destination
        self.price = price

    def __str__(self):
        """
        Returnează o reprezentare text a pachetului.

        Returns:
            str: Reprezentarea text a pachetului.
        """
        return f"{self.destination} ({self.start_date.strftime('%Y-%m-%d')} - {self.end_date.strftime('%Y-%m-%d')}): {self.price} Euro"
