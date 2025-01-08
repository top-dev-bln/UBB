class Student:

    def __init__(self, id_student,nume, grup):
        self.__id_student = id_student
        self.__nume = nume
        self.__grup = grup


    def get_id_student(self):
        """
        Returnează ID-ul studentului.

        Returnează:
            int: ID-ul studentului.
        """
        return self.__id_student
    
    def get_nume(self):
        """
        Returnează numele studentului.

        Returnează:
            str: Numele studentului.
        """
        return self.__nume
    def get_grup(self):
        """
        Returnează grupa studentului.

        Returnează:
            int: Grupa studentului.
        """
        return self.__grup
    
    def set_nume(self, nume):
        """
        Setează numele studentului.

        Parametri:
            nume (str): Noul nume al studentului.
        """
        self.__nume = nume

    def set_grup(self, grup):
        """
        Setează grupa studentului.

        Parametri:
            grup (int): Noua grupă a studentului.
        """
        self.__grup = grup


    
    def __str__(self):
        return f"[{self.__id_student}] {self.__nume} - {self.__grup}"