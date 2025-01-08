class Laborator:

    def __init__(self, num_laborator:int, num_problema:int, descriere:str, deadline):
        self.__num_laborator = num_laborator
        self.__num_problema = num_problema
        self.__descriere = descriere
        self.__deadline = deadline

    def get_numar_laborator(self):
        """
        Returnează numărul laboratorului.

        Returnează:
            int: Numărul laboratorului.
        """
        return self.__num_laborator

    def get_numar_problema(self):
        """
        Returnează numărul problemei.

        Returnează:
            int: Numărul problemei.
        """
        return self.__num_problema

    def get_descriere(self):
        """
        Returnează descrierea problemei de laborator.

        Returnează:
            str: Descrierea problemei de laborator.
        """
        return self.__descriere

    def get_deadline(self):
        """
        Returnează termenul limită al problemei de laborator.

        Returnează:
            datetime.date: Termenul limită al problemei de laborator.
        """
        return self.__deadline
    
    def set_descriere(self, descriere:str):
        """
        Setează descrierea problemei de laborator.

        Parametri:
            descriere (str): Descrierea problemei de laborator.
        """
        self.__descriere = descriere

    def set_deadline(self, deadline):
        """
        Setează termenul limită al problemei de laborator.

        Parametri:
            deadline (datetime.date): Termenul limită al problemei de laborator.
        """
        self.__deadline = deadline

    def __str__(self):
        """
        Returnează o reprezentare textuală a laboratorului.

        Returnează:
            str: Reprezentarea textuală a laboratorului.
        """
        return "Laboratorul " + str(self.__num_laborator) + " Problema " + str(self.__num_problema) + " Descriere " + self.__descriere + " Deadline " + str(self.__deadline)