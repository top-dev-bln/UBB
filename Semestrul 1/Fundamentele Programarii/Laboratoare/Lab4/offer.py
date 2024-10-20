from datetime import datetime
import uuid
class Package:
    def __init__(self, start_date:datetime, end_date:datetime, destination:str, price:float)->None:
        """
        Initializare instanta de oferta cu data de inceput , data de final , destinatie si pret

        :param start_date: Data la care începe călătoria (str)
        :param end_date: Data la care se încheie călătoria (str)
        :param destination: Destinația călătoriei (str)
        :param price: Prețul călătoriei (float)
        """
        self.start_date = start_date
        self.end_date = end_date
        self.destination = destination
        self.price = price

    def __str__(self):
        """
        Returnează o reprezentare text a ofertei.
        """
        return f"Pachetul pentru {self.destination} din data de {self.start_date.strftime("%%Y-%%m-%%d")} pana {self.end_date.strftime("%%Y-%%m-%%d")} este la pretul de {self.price} Euro."
