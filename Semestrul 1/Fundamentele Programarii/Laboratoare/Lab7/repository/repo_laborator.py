from utils.utils import generate_id


class RepoLaborator:

    def __init__(self):
        """
        Inițializează un nou depozit pentru laboratoare.
        """
        self.__laboratoare = {}

    def adauga_laborator(self, laborator):
        """
        Adaugă un laborator în depozit.

        Parametri:
            laborator (Laborator): Laboratorul de adăugat.

        Ridică:
            ValueError: Dacă există deja un laborator cu același număr.
        """
        lab = laborator.get_numar_laborator()
        prb = laborator.get_numar_problema()
        id = generate_id(lab, prb)
        if id in self.__laboratoare:
            raise ValueError("laborator cu acelasi numar existent!")
        self.__laboratoare[id] = laborator
        
    def sterge_laborator(self, lab, prb):
        """
        Șterge un laborator din depozit.

        Parametri:
            lab (int): Numărul laboratorului.
            prb (int): Numărul problemei.

        Ridică:
            ValueError: Dacă laboratorul nu există.
        """
        id_laborator = generate_id(lab, prb)
        if id_laborator not in self.__laboratoare:
            raise ValueError("laborator inexistent!")
        del self.__laboratoare[id_laborator]

    def modifica_laborator(self, laborator):
        """
        Modifică un laborator din depozit.

        Parametri:
            laborator (Laborator): Laboratorul de modificat.

        Ridică:
            ValueError: Dacă laboratorul nu există.
        """
        lab = laborator.get_numar_laborator()
        prb = laborator.get_numar_problema()
        id = generate_id(lab, prb)
        if id not in self.__laboratoare:
            raise ValueError("laborator inexistent!")
        self.__laboratoare[id].set_descriere(laborator.get_descriere())
        self.__laboratoare[id].set_deadline(laborator.get_deadline())



    def get_laborator(self, lab, prb):
        """
        Returnează un laborator din depozit.

        Parametri:
            lab (int): Numărul laboratorului.
            prb (int): Numărul problemei.

        Returnează:
            Laborator: Laboratorul cerut.
        """
        id_laborator = generate_id(lab, prb)
        if id_laborator not in self.__laboratoare:
            raise ValueError("laborator inexistent!")
        return self.__laboratoare[id_laborator]
    
    
    def get_all(self):
        """
        Returnează toate laboratoarele din depozit.

        Returnează:
            dict_values: Valorile din dicționarul de laboratoare.
        """
        return self.__laboratoare.values()