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
    #todo testing
    pass



test()


  