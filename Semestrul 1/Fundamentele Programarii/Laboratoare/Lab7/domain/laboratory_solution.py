
class LaboratorySolution:
    def __init__(self, student_id: int, lab_number: int, problem_number: int, solution: str, grade: float = None):
        self.__student_id = student_id
        self.__lab_number = lab_number
        self.__problem_number = problem_number
        self.__solution = solution
        self.__grade = grade

    def get_student_id(self):
        return self.__student_id

    def get_lab_number(self):
        return self.__lab_number

    def get_problem_number(self):
        return self.__problem_number

    def get_solution(self):
        return self.__solution

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade: float):
        self.__grade = grade

    def __str__(self):
        grade_str = f"Grade: {self.__grade}" if self.__grade is not None else "Not graded yet"
        return f"Solution for Lab {self.__lab_number} Problem {self.__problem_number} by Student {self.__student_id}\n" \
               f"Solution: {self.__solution}\n{grade_str}"