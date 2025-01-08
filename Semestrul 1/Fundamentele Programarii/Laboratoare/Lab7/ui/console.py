import datetime

class Consola:

    def __init__(self,_service_studenti, _service_laboratoare):
        self.__service_studenti = _service_studenti
        self.__service_laboratoare = _service_laboratoare

    
    @staticmethod
    def afiseaza_meniu():
        print("1. Adauga student")
        print("2. Afiseaza studentii")
        print("3. Adauga laborator")
        print("4. Afiseaza laboratoare")
        print("5. Afisare detalii student")
        print("6. Afisare detalii laborator")
        print("7. Asignare laborator student")
        print("8. Notare laborator")
        print("9. Afisare solutii")
        print("10. Trimite solutie")
        print("11. Sterge student")
        print("12. Sterge laborator")
        print("13. Modifica student")
        print("14. Modifica laborator")
        print("15. Afisare studenti cu note")
        print("16. Afisare studenti picati")
        print("17. Media Notelor studentilor")
        print("18. Afisare asignari")
        print("x. Iesire")


    def __adauga_student_ui(self):
        try:
            print("introduceti datele studentului:")
            id= int(input("id:"))
            nume = input("nume:")
            grup = int(input("grup:"))

            self.__service_studenti.adauga_student(id, nume, grup)
            print("student adaugat cu succes!")
        except Exception as ex:
            print(ex)

    def __afiseaza_studenti_ui(self):
        studenti = self.__service_studenti.get_all_studenti()
        if len(studenti) == 0:
            print("nu exista studenti!")
            return
        print("studentii sunt:")
        for student in studenti:
            print(student)


    def __sterge_student_ui(self):
        try:
            id = int(input("introduceti id-ul studentului:"))
            self.__service_studenti.sterge_student(id)
            print("student sters cu succes!")
        except Exception as ex:
            print(ex)

    def __modifica_student_ui(self):
        try:
            print("introduceti id-ul studentului:")
            id = int(input("id:"))
            print("introduceti noile date:")
            nume = input("nume:")
            grup = int(input("grup:"))

            self.__service_studenti.modifica_student(id, nume, grup)
            print("student modificat cu succes!")
        except Exception as ex:
            print(ex)


    def __afisare_detalii_student_ui(self):
        try:
            print("introduceti id-ul sau numele studentului:")
            nume = input("introduceti numele studentului:")
            student = self.__service_studenti.get_student_by_name(nume)
            print(student)
        except Exception as ex:
            print(ex)



    def __adauga_laborator_ui(self):
        try:
            print("introduceti datele laboratorului:")
            lab = int(input("numar laborator:"))
            prb = int(input("numar problema:"))
            descriere = input("descriere:")
            print("introduceti deadline-ul:")
            ziua = int(input("Ziua: "))
            luna = int(input("Luna: "))
            anul = int(input("Anul: "))
        
            deadline = datetime.date(anul, luna, ziua)
        except ValueError as ve:
            print(ve)
            return
        try:
            self.__service_laboratoare.adauga_laborator(lab, prb, descriere, deadline)
            print("laborator adaugat cu succes!")
        except Exception as ex:
            print(ex)


    def __sterge_laborator_ui(self):
        try:
            print("introduceti datele laboratorului:")
            lab = int(input("numar laborator:"))
            prb = int(input("numar problema:"))

            self.__service_laboratoare.sterge_laborator(lab, prb)
            print("laborator sters cu succes!")
        except Exception as ex:
            print(ex)


    def __modifica_laborator_ui(self):
        try:
            print("introduceti datele laboratorului:")
            lab = int(input("numar laborator:"))
            prb = int(input("numar problema:"))

            print("introduceti noile date:")
            descriere = input("descriere:")
            print("introduceti deadline-ul:")
            ziua = int(input("Ziua: "))
            luna = int(input("Luna: "))
            anul = int(input("Anul: "))
        

            deadline = datetime.date(anul, luna, ziua)
        except ValueError as ve:
            print(ve)
            return
        try:
            self.__service_laboratoare.modifica_laborator(lab, prb, descriere, deadline)
            print("laborator modificat cu succes!")
        except Exception as ex:
            print(ex)

    def __afiseaza_laboratoare_ui(self):
        laboratoare = self.__service_laboratoare.get_all_laboratoare()
        if len(laboratoare) == 0:
            print("nu exista laboratoare!")
            return
        print("laboratoarele sunt:")
        for laborator in laboratoare:
            print(laborator)

    def __afisare_detalii_laborator_ui(self):
        try:
            print("introduceti datele laboratorului:")
            lab = int(input("numar laborator:"))
            prb = int(input("numar problema:"))

            laborator = self.__service_laboratoare.get_laborator(lab, prb)
            print(laborator)
        except Exception as ex:
            print(ex)

    def __asignare_laborator_student_ui(self):
        try:
            student_id = int(input("Enter student ID: "))
            lab_number = int(input("Enter laboratory number: "))
            problem_number = int(input("Enter problem number: "))
            
            self.__service_laboratoare.assign_laboratory(student_id, lab_number, problem_number)
            print("Laboratory successfully assigned!")
        except Exception as ex:
            print(ex)

    def __trimite_solutie_ui(self):
        try:
            student_id = int(input("Enter student ID: "))
            lab_number = int(input("Enter laboratory number: "))
            problem_number = int(input("Enter problem number: "))
            solution = input("Enter your solution: ")
            
            self.__service_laboratoare.submit_solution(student_id, lab_number, problem_number, solution)
            print("Solution submitted successfully!")
        except Exception as ex:
            print(ex)

    def __notare_laborator_ui(self):
        try:
            student_id = int(input("Enter student ID: "))
            lab_number = int(input("Enter laboratory number: "))
            problem_number = int(input("Enter problem number: "))
            grade = float(input("Enter grade (0-10): "))
            
            if grade < 0 or grade > 10:
                raise ValueError("Grade must be between 0 and 10")
                
            self.__service_laboratoare.grade_solution(student_id, lab_number, problem_number, grade)
            print("Solution graded successfully!")
        except Exception as ex:
            print(ex)

    def __afisare_solutii_ui(self):
        try:
            lab_number = int(input("Enter laboratory number (or 0 for all): "))
            solutions = self.__service_laboratoare.get_solutions(lab_number if lab_number != 0 else None)
            
            if not solutions:
                print("No solutions found!")
                return
                
            print("\nSolutions:")
            for solution in solutions:
                print("\n" + str(solution))
        except Exception as ex:
            print(ex)

    def __afisare_studenti_note_ui(self):
        try:
            lab_number = int(input("Enter laboratory number: "))
            problem_number = int(input("Enter problem number: "))
            students_grades = self.__service_laboratoare.get_students_grades_for_lab(lab_number, problem_number)
            
            if not students_grades:
                print("No students found for this lab and problem!")
                return
                
            print("\nStudents and their grades:")
            for student_id, grade in students_grades:
                grade_str = grade if grade is not None else "Not graded yet"
                print(f"Student ID: {student_id}, Grade: {grade_str}")
        except Exception as ex:
            print(ex)

    def __afisare_studenti_picati_ui(self):
        try:
            students_below_5 = self.__service_laboratoare.get_students_with_grades_below_5()
            
            if not students_below_5:
                print("No students with grades below 5 found!")
                return
                
            print("\nStudents with grades below 5:")
            for student_id, lab_number, problem_number, grade in students_below_5:
                print(f"Student ID: {student_id}, Lab: {lab_number}, Problem: {problem_number}, Grade: {grade}")
        except Exception as ex:
            print(ex)


    def __afisare_medii(self):
        try:
            students_avg = self.__service_laboratoare.get_students_with_average_grade()
            
            if not students_avg:
                print("No students found!")
                return
                
            print("\nStudents and their average grades:")
            for student_id, avg in students_avg:
                print(f"Student ID: {student_id}, Average grade: {avg}")
        except Exception as ex:
            print(ex)

    def __afisare_asignari(self):
        stud_id = int(input("Enter student ID: "))
        try:
            assignments = self.__service_laboratoare.get_assignments(stud_id)
            
            if not assignments:
                print("No assignments found!")
                return
                
            print("\nAssignments:")
            for lab_number, problem_number in assignments:
                print(f"Lab: {lab_number}, Problem: {problem_number}")
        except Exception as ex:
            print(ex)
        
        

    def run(self):
        is_running = True
        while is_running:
            self.afiseaza_meniu()
            optiune = input(">>>").upper().strip()
            match optiune:
                case '1':
                    self.__adauga_student_ui()
                case '2':
                    self.__afiseaza_studenti_ui()
                case '3':
                    self.__adauga_laborator_ui()
                case '4':
                    self.__afiseaza_laboratoare_ui()
                case '5':
                    self.__afisare_detalii_student_ui()
                case '6':
                    self.__afisare_detalii_laborator_ui()
                case '7':
                    self.__asignare_laborator_student_ui()
                case '8':
                    self.__notare_laborator_ui()
                case '9':
                    self.__afisare_solutii_ui()
                case '10':
                    self.__trimite_solutie_ui()
                case '11':
                    self.__sterge_student_ui()
                case '12':
                    self.__sterge_laborator_ui()
                case '13':
                    self.__modifica_student_ui()
                case '14':
                    self.__modifica_laborator_ui()
                case '15':
                    self.__afisare_studenti_note_ui()
                case '16':
                    self.__afisare_studenti_picati_ui()
                case '17':
                    self.__afisare_medii()
                case '18':
                    self.__afisare_asignari()
                case 'X':
                    is_running = False
