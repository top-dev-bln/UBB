from utils.utils import generate_id
import datetime

class Teste:



    def test_student():
        from domain.student import Student
        student = Student(1, 'Andrei', 211)
        assert student.get_id_student() == 1
        assert student.get_nume() == 'Andrei'
        assert student.get_grup() == 211
        student.set_nume('Mihai')
        student.set_grup(212)
        assert student.get_nume() == 'Mihai'
        assert student.get_grup() == 212


    
    def test_student_repo():
        from repository.repo_studenti import RepoStudenti
        from domain.student import Student
        repo = RepoStudenti()
        student = Student(1, 'Andrei', 211)
        repo.adauga_student(student)
        assert repo.get_all() == [student]
        repo.sterge_student(1)
        assert repo.get_all() == []


    def test_laborator():
        from domain.laborator import Laborator
        laborator = Laborator(1, 1, "test", datetime.date(2024, 5, 1))
        assert laborator.get_numar_laborator() == 1
        assert laborator.get_numar_problema() == 1
        assert laborator.get_deadline() == datetime.date(2024, 5, 1)
        assert laborator.get_descriere() == "test"
        laborator.set_descriere("test2")
        laborator.set_deadline(datetime.date(2024, 5, 2))
        assert laborator.get_descriere() == "test2"
        assert laborator.get_deadline() == datetime.date(2024, 5, 2)


    def test_laborator_repo():
        from repository.repo_laborator import RepoLaborator
        from domain.laborator import Laborator
        repo_lab = RepoLaborator()
        laborator = Laborator(1, 1, "test", datetime.date(2024, 5, 1))
        repo_lab.adauga_laborator(laborator)
        assert list(repo_lab.get_all()) == [laborator]
        repo_lab.sterge_laborator(1, 1)
        assert list(repo_lab.get_all()) == []


        
        


    def test_generate_id():
        assert generate_id(1, 2) == generate_id(1, 2)
        assert generate_id(1, 2) != generate_id(1, 3)
        assert generate_id(1, 2) != generate_id(2, 1)
        assert generate_id(1, 2) != generate_id(2, 3)

    def test_laboratory_solution():
        from domain.laboratory_solution import LaboratorySolution
        solution = LaboratorySolution(1, 1, 1, "This is a solution")
        assert solution.get_student_id() == 1
        assert solution.get_lab_number() == 1
        assert solution.get_problem_number() == 1
        assert solution.get_solution() == "This is a solution"
        assert solution.get_grade() is None
        solution.set_grade(9.5)
        assert solution.get_grade() == 9.5

    def test_service_laborator():
        from domain.validator_laborator import ValidatorLaborator
        from repository.repo_laborator import RepoLaborator
        from service.service_laborator import ServiceLaborator
        from domain.laborator import Laborator

        validator = ValidatorLaborator()
        repo = RepoLaborator()
        service = ServiceLaborator(validator, repo)

        # Test adauga_laborator
        laborator = Laborator(1, 1, "test", datetime.date(2024, 5, 1))
        service.adauga_laborator(1, 1, "test", datetime.date(2024, 5, 1))
        assert len(service.get_all_laboratoare()) == 1

        # Test assign_laboratory
        service.assign_laboratory(1, 1, 1)
        try:
            service.assign_laboratory(1, 1, 1)
        except ValueError as ve:
            assert str(ve) == "Laboratory already assigned to this student!"

        # Test submit_solution
        service.submit_solution(1, 1, 1, "This is a solution")
        solutions = service.get_solutions()
        assert len(solutions) == 1
        assert solutions[0].get_solution() == "This is a solution"

        # Test grade_solution
        service.grade_solution(1, 1, 1, 9.5)
        assert solutions[0].get_grade() == 9.5

        # Test get_students_grades_for_lab
        students_grades = service.get_students_grades_for_lab(1, 1)
        assert len(students_grades) == 1
        assert students_grades[0] == (1, 9.5)

        # Test get_students_with_grades_below_5
        service.grade_solution(1, 1, 1, 4.0)
        students_below_5 = service.get_students_with_grades_below_5()
        assert len(students_below_5) == 1
        assert students_below_5[0] == (1, 1, 1, 4.0)

    @staticmethod
    def ruleaza_toate_testele():
        Teste.test_student()
        Teste.test_student_repo()
        Teste.test_laborator()
        Teste.test_laborator_repo()
        Teste.test_generate_id()
        Teste.test_laboratory_solution()
        Teste.test_service_laborator()
        print("Toate testele au trecut cu succes!")


    # def test_service_studenti():
    #     from domain.validator_student import ValidatorStudent
    #     from repository.repo_studenti import RepoStudenti
    #     from service.service_studenti import ServiceStudenti

    #     validator = ValidatorStudent()
    #     repo = RepoStudenti()
    #     service = ServiceStudenti(validator, repo)

    #     # Test adauga_student
    #     service.adauga_student(1, 'nume', 211)
    #     studenti = service.get_all_studenti()
    #     assert len(studenti) == 1
    #     assert studenti[0].get_id_student() == 1
    #     assert studenti[0].get_nume() == 'nume'
    #     assert studenti[0].get_grup() == 211

    #     # Test sterge_student
    #     service.sterge_student(1)
    #     studenti = service.get_all_studenti()
    #     assert len(studenti) == 0

    #     # Test modifica_student
    #     service.adauga_student(1, 'nume', 1)
    #     service.modifica_student(1, 'alt nume', 211)
    #     studenti = service.get_all_studenti()
    #     assert studenti[0].get_nume() == 'alt nume'
    #     assert studenti[0].get_grup() == 211

    # def test_repo_studenti():
    #     from domain.student import Student
    #     from repository.repo_studenti import RepoStudenti

    #     repo = RepoStudenti()

    #     # Test adauga_student
    #     student = Student(1, 'nume', 211)
    #     repo.adauga_student(student)
    #     studenti = repo.get_all()
    #     assert len(studenti) == 1
    #     assert studenti[0].get_id_student() == 1
    #     assert studenti[0].get_nume() == 'nume'
    #     assert studenti[0].get_grup() == 211

    #     # Test sterge_student
    #     repo.sterge_student(1)
    #     studenti = repo.get_all()
    #     assert len(studenti) == 0

    #     # Test modifica_student
    #     student = Student(1, 'nume', 211)
    #     repo.adauga_student(student)
    #     student_modificat = Student(1, 'alt nume', 211)
    #     repo.modifica_student(student_modificat)
    #     studenti = repo.get_all()