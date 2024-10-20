class Package:
    def __init__(self, start_date:str, end_date:str, destination:str, price:float)->None:
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









def test():
    #todo testingaww
    pass



test()


  














  
'''


    def __str__(self):
        """
        Returnează o reprezentare șir a ofertei.
        """
        return f"Vacanta la {self.destination} din data de {self.start_date} pana {self.end_date} la pretul de {self.price} Euro."


  def update_offer(self, start_date=None, end_date=None, destination=None, price=None):
        """
        Update the offer details with the provided information. Only non-None values are updated.
        
        :param start_date: New start date (string or datetime), optional
        :param end_date: New end date (string or datetime), optional
        :param destination: New destination (string), optional
        :param price: New price (float), optional
        """
        if start_date:
            self.start_date = start_date
        if end_date:
            self.end_date = end_date
        if destination:
            self.destination = destination
        if price:
            self.price = price

    def duration(self):
        """
        Returns the duration of the trip in days.
        Assuming start_date and end_date are in datetime format.
        """
        return (self.end_date - self.start_date).days

    def is_in_price_range(self, max_price):
        """
        Check if the offer's price is within a given price range.
        
        :param max_price: Maximum acceptable price (float)
        :return: True if the offer's price is less than or equal to max_price, False otherwise
        """
        return self.price <= max_price

    def is_within_dates(self, start_interval, end_interval):
        """
        Check if the offer's trip is within the specified date interval.
        
        :param start_interval: Start of the desired interval (datetime)
        :param end_interval: End of the desired interval (datetime)
        :return: True if the offer's trip is within the interval, False otherwise
        """
        return self.start_date >= start_interval and self.end_date <= end_interval
'''