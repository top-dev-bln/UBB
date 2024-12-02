import string
from domain.student import Student
import random

class ServiceStudenti:

    def __init__(self,_validator_student,_repo_studenti, _service_laborator):
        """
        Inițializează un obiect de tip service_studenti.

        Parametri:
            _validator_student: Validatorul pentru obiectele de tip student.
            _repo_studenti: Repozitoriul pentru obiectele de tip student.
            _service_laborator: Service-ul pentru laboratoare.
        """
        self.__validator_student = _validator_student
        self.__repo_studenti = _repo_studenti
        self.__service_laborator = _service_laborator

    def adauga_student(self,id_student:int,nume:str,grup:int):
        """
        Adauga un student in repository.

        Parametrii:
            id_student (int): ID-ul studentului.
            nume (str): Numele studentului.
            grup (int): Grupul din care face parte studentul.

        Raises:
            ValidationException: Daca studentul nu este valid.
            RepositoryException: Daca studentul exista deja in repository.
        """
        student = Student(id_student,nume,grup)
        self.__validator_student.valideaza_student(student)
        self.__repo_studenti.adauga_student(student)

    def sterge_student(self,id_student:int):
        """
        Șterge un student din repository și toate soluțiile și notele asociate.

        Parametri:
        id_student (int): ID-ul studentului care trebuie șters.

        Returnează:
        None
        """
        self.__repo_studenti.sterge_student(id_student)
        self.__service_laborator.sterge_student(id_student)

    def modifica_student(self,id_student:int,nume:str,grup:int):
        """
        Modifică un student din repository.

        Parametri:
        id_student (int): ID-ul studentului care trebuie modificat.
        nume (str): Noul nume al studentului.
        grup (int): Noul grup al studentului.

        Returnează:
        None
        """
        student = Student(id_student,nume,grup)
        self.__validator_student.valideaza_student(student)
        self.__repo_studenti.modifica_student(student)


    def modifica_student(self, id_student, nume, grup):
        """
        Modifică un student existent în sistem.

        Args:
            id_student (int): ID-ul studentului care trebuie modificat.
            nume (str): Noul nume al studentului.
            grup (str): Noul grup al studentului.

        Raises:
            ValidationException: Dacă datele studentului nu sunt valide.
            RepositoryException: Dacă studentul nu există în repository.
        """
        student = Student(id_student, nume, grup)
        self.__validator_student.valideaza_student(student)
        self.__repo_studenti.modifica_student(student)

    def get_student_by_name(self, nume):
        """
        Returnează studentul cu numele dat.

        Parametri:
            nume (str): Numele studentului căutat.

        Returnează:
            Student: Studentul cu numele dat.
        """
        return self.__repo_studenti.get_student_by_name(nume)
    



    #### lab 8

    def generate_random_students(self, numar_studenti):
        """
        Generează un număr dat de studenți cu date aleatoare.

        Args:
            numar_studenti (int): Numărul de studenți care trebuie generați.

        Returns:
            None
        """
        count = 0
        while count < numar_studenti:
            id_student = random.randint(1, 9999)
            grupa = random.randint(211, 216)
            nume_random = ''.join(random.choices(string.ascii_letters, k=10))  
            try:
                self.adauga_student(id_student, nume_random, grupa)
                count += 1
            except Exception as e:
                pass


        
    
    def get_all_studenti(self):
        return self.__repo_studenti.get_all()