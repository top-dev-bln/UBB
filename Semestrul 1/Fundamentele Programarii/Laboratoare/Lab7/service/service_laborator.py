from domain.laborator import Laborator
import random
import string
import datetime
from domain.laboratory_solution import LaboratorySolution

class ServiceLaborator:

    def __init__(self, _validator_laborator, _repo_laboratoare):
        """
        Inițializează un nou serviciu pentru laboratoare.

        Parametri:
            _validator_laborator (ValidatorLaborator): Validatorul pentru laboratoare.
            _repo_laboratoare (RepoLaborator): Repository-ul pentru laboratoare.
        """
        self.__validator_laborator = _validator_laborator
        self.__repo_laboratoare = _repo_laboratoare
        self.__solutions = {}  
        self.__assignments = {}  

    def adauga_laborator(self, numar_laborator:int, numar_problema:int, descriere:str, deadline):
        """
        Adaugă un laborator.

        Parametri:
            numar_laborator (int): Numărul laboratorului.
            numar_problema (int): Numărul problemei.
            descriere (str): Descrierea problemei.
            deadline (datetime.date): Termenul limită al problemei.

        Returnează:
            None
        """
        laborator = Laborator(numar_laborator, numar_problema, descriere, deadline)
        self.__validator_laborator.valideaza_laborator(laborator)
        self.__repo_laboratoare.adauga_laborator(laborator)
    
    def sterge_laborator(self, numar_laborator:int, numar_problema:int):
        """
        Șterge un laborator și toate soluțiile și notele asociate.

        Parametri:
            numar_laborator (int): Numărul laboratorului.
            numar_problema (int): Numărul problemei.

        Returnează:
            None
        """
        self.__repo_laboratoare.sterge_laborator(numar_laborator, numar_problema)
        
        self.__solutions = {key: value for key, value in self.__solutions.items() if not (key[1] == numar_laborator and key[2] == numar_problema)}
        
        for student_id in self.__assignments:
            self.__assignments[student_id] = [assignment for assignment in self.__assignments[student_id] if assignment != (numar_laborator, numar_problema)]

    def modifica_laborator(self, numar_laborator:int, numar_problema:int, descriere:str, deadline):
        """
        Modifică un laborator.

        Parametri:
            numar_laborator (int): Numărul laboratorului.
            numar_problema (int): Numărul problemei.
            descriere (str): Noua descriere a problemei.
            deadline (datetime.date): Noul termen limită al problemei.

        Returnează:
            None
        """
        laborator = Laborator(numar_laborator, numar_problema, descriere, deadline)
        self.__validator_laborator.valideaza_laborator(laborator)
        self.__repo_laboratoare.modifica_laborator(laborator)

    def get_all_laboratoare(self):
        """
        Returnează toate laboratoarele.

        Returnează:
            list: Lista cu toate laboratoarele.
        """
        return self.__repo_laboratoare.get_all()
    
    def get_laborator(self, numar_laborator:int, numar_problema:int):
        """
        Returnează un laborator.

        Parametri:
            numar_laborator (int): Numărul laboratorului.
            numar_problema (int): Numărul problemei.

        Returnează:
            Laborator: Laboratorul cerut.
        """
        return self.__repo_laboratoare.get_laborator(numar_laborator, numar_problema)

    def modifica_laborator(self, numar_laborator, numar_problema, descriere, deadline):
        laborator = Laborator(numar_laborator, numar_problema, descriere, deadline)
        self.__validator_laborator.valideaza_laborator(laborator)
        self.__repo_laboratoare.modifica_laborator(laborator)


    def generate_random_laboratoare(self, numar_laboratoare):
        """
        Generează un număr dat de laboratoare cu date aleatoare.

        Args:
            numar_laboratoare (int): Numărul de laboratoare care trebuie generate.

        Returns:
            None
        """
        count = 0
        while count < numar_laboratoare:
            nr_lab = random.randint(1, 12)
            nr_prb = random.randint(1, 12)
            descriere = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            ziua = random.randint(1, 28)
            luna = random.randint(1, 12)
            anul = random.randint(2020, 2024)
            deadline = datetime.date(anul, luna, ziua)
            try:
                self.adauga_laborator(nr_lab, nr_prb, descriere, deadline)
                count += 1
            except ValueError as e:
                print(f"Failed to add laborator {nr_lab}-{nr_prb}: {e}  - {anul}")

    def assign_laboratory(self, student_id: int, lab_number: int, problem_number: int):
        """
        Asignează un laborator unui student.

        Parametri:
            student_id (int): ID-ul studentului.
            lab_number (int): Numărul laboratorului.
            problem_number (int): Numărul problemei.

        Returnează:
            None
        """
        self.get_laborator(lab_number, problem_number)
        
        if student_id not in self.__assignments:
            self.__assignments[student_id] = []
        
        assignment = (lab_number, problem_number)
        if assignment in self.__assignments[student_id]:
            raise ValueError("Laboratory already assigned to this student!")
            
        self.__assignments[student_id].append(assignment)

    def get_assignments(self, student_id):
        """
        Returnează laboratoarele asignate unui student.

        Parametri:
            student_id (int): ID-ul studentului.

        Returnează:
            list: Lista de tuple (lab_number, problem_number).
        """
        if student_id not in self.__assignments:
            return []
        return self.__assignments[student_id]
        

    def submit_solution(self, student_id: int, lab_number: int, problem_number: int, solution: str):
        """
    Trimite soluția unui laborator.

    Parametri:
        student_id (int): ID-ul studentului.
        lab_number (int): Numărul laboratorului.
        problem_number (int): Numărul problemei.
        solution (str): Soluția trimisă.

    Returnează:
        None
    """
        if student_id not in self.__assignments or (lab_number, problem_number) not in self.__assignments[student_id]:
            raise ValueError("Laboratory not assigned to this student!")
            
        solution_key = (student_id, lab_number, problem_number)
        self.__solutions[solution_key] = LaboratorySolution(student_id, lab_number, problem_number, solution)

    def grade_solution(self, student_id: int, lab_number: int, problem_number: int, grade: float):
        """
    Notează soluția unui laborator.

    Parametri:
        student_id (int): ID-ul studentului.
        lab_number (int): Numărul laboratorului.
        problem_number (int): Numărul problemei.
        grade (float): Nota acordată.

    Returnează:
        None
    """
        solution_key = (student_id, lab_number, problem_number)
        if solution_key not in self.__solutions:
            raise ValueError("No solution found for this laboratory!")
            
        self.__solutions[solution_key].set_grade(grade)

    def get_solutions(self, lab_number=None):
        """
    Returnează soluțiile pentru un laborator.

    Parametri:
        lab_number (int, optional): Numărul laboratorului. Dacă nu este specificat, returnează toate soluțiile.

    Returnează:
        list: Lista soluțiilor.
    """
        if lab_number is None:
            return list(self.__solutions.values())
        return [s for s in self.__solutions.values() if s.get_lab_number() == lab_number]

    def get_students_grades_for_lab(self, lab_number: int, problem_number: int):
        """
        Returnează lista de studenți și notele lor pentru un laborator și o problemă specifică.

        Parametri:
            lab_number (int): Numărul laboratorului.
            problem_number (int): Numărul problemei.

        Returnează:
            list: Lista de tuple (student_id, grade).
        """
        students_grades = []
        for key, solution in self.__solutions.items():
            if solution.get_lab_number() == lab_number and solution.get_problem_number() == problem_number:
                students_grades.append((solution.get_student_id(), solution.get_grade()))
        return students_grades
    

    def get_students_with_grades_below_5(self):
        """
        Returnează lista de studenți care au primit note mai mici de 5.

        Returnează:
            list: Lista de tuple (student_id, lab_number, problem_number, grade).
        """
        students_below_5 = []
        for key, solution in self.__solutions.items():
            if solution.get_grade() is not None and solution.get_grade() < 5:
                students_below_5.append((solution.get_student_id(), solution.get_lab_number(), solution.get_problem_number(), solution.get_grade()))
        return students_below_5
    
    def get_students_with_average_grade(self):
        """
        Returnează lista de studenți și media notelor lor.

        Returnează:
            list: Lista de tuple (student_id, average_grade).
        """
        students_grades = {}
        for key, solution in self.__solutions.items():
            if solution.get_grade() is not None:
                if solution.get_student_id() not in students_grades:
                    students_grades[solution.get_student_id()] = []
                students_grades[solution.get_student_id()].append(solution.get_grade())
        
        students_average_grades = []
        for student_id, grades in students_grades.items():
            average_grade = sum(grades) / len(grades)
            students_average_grades.append((student_id, average_grade))
        return students_average_grades

    def sterge_student(self, student_id: int):
        """
        Șterge un student și toate soluțiile și notele asociate.

        Parametri:
            student_id (int): ID-ul studentului.

        Returnează:
            None
        """
        if student_id in self.__assignments:
            del self.__assignments[student_id]
        
        self.__solutions = {key: value for key, value in self.__solutions.items() if key[0] != student_id}