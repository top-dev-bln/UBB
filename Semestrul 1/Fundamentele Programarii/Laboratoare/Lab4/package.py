from datetime import datetime

class Package:
    def __init__(self, start: datetime, end: datetime, destination: str, price: float):
        self.start_date = start
        self.end_date = end
        self.destination = destination
        self.price = price

    def __str__(self):
        return f"{self.destination} ({self.start_date.strftime('%Y-%m-%d')} - {self.end_date.strftime('%Y-%m-%d')}): {self.price} Euro"
