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
        print("9. Afisare studenti cu note")
        print("10. Afisare studenti picati")
        print("11. Sterge student")
        print("12. Sterge laborator")
        print("13. Modifica student")
        print("14. Modifica laborator")
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


# lab 8

    def __generate_random_student_ui(self):
        numar_studenti = int(input("introduceti numarul de studenti generati aleatoriu:"))
        self.__service_studenti.generate_random_students(numar_studenti)
        print("studenti generati random cu succes!")

    def __generate_random_laborator_ui(self):
        numar_laboratoare = int(input("introduceti numarul de laboratoare generati aleatoriu:"))
        self.__service_laboratoare.generate_random_laboratoare(numar_laboratoare)
        numar_labs = len(self.__service_laboratoare.get_all_laboratoare())
        print(f"{numar_labs} laboratoare generate random cu succes!")



    def run(self):
        is_running = True

        
        while is_running:
            self.afiseaza_meniu()
            optiune = input(">>>").upper().strip()
            match optiune:
                case '0':
                    self.__generate_random_student_ui()
                    self.__generate_random_laborator_ui()
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
                    self.__afisare_studenti_note_ui()
                case '10':
                    self.__afisare_studenti_picati_ui()
                case '11':
                    self.__sterge_student_ui()
                case '12':
                    self.__sterge_laborator_ui()
                case '13':
                    self.__modifica_student_ui()
                case '14':
                    self.__modifica_laborator_ui()
                case 'X':
                    is_running = False
