class RepoStudenti:

    def __init__(self):
        self.__studenti = []

    def adauga_student(self,student):
        """
        Adauga un student in repository.

        Parametrii:
            student (Student): Obiectul student care trebuie adaugat.

        Raises:
            ValueError: Daca exista deja un student cu acelasi ID in repository.
        """
        if student.get_id_student() in self.__studenti:
            raise ValueError("student cu acelasi id existent!")
        self.__studenti.append({"id": student.get_id_student() , "stud":student})

    def sterge_student(self,id_student:int):
        """
        Șterge un student din repository.

        Parametri:
        id_student (int): ID-ul studentului care trebuie șters.

        Ridică:
        ValueError: Dacă studentul cu ID-ul specificat nu există în repository.
        """
        if id_student not in self.__studenti:
            raise ValueError("student inexistent!")
        del self.__studenti[id_student]

    def modifica_student(self,student):
        """
        Modifică un student din repository.

        Parametri:
        student (Student): Obiectul student care trebuie modificat.

        Ridică:
        ValueError: Dacă studentul cu ID-ul specificat nu există în repository.
        """
        if student.get_id_student() not in self.__studenti:
            raise ValueError("student inexistent!")
        self.__studenti[student.get_id_student()].set_nume(student.get_nume())
        self.__studenti[student.get_id_student()].set_grup(student.get_grup())

    def get_all(self):
        return [stud["stud"] for stud in self.__studenti]

    def sterge_student(self, id_student):
        """
        Sterge un student din lista de studenti pe baza ID-ului.

        Args:
            id_student (int): ID-ul studentului care trebuie sters.

        Raises:
            ValueError: Daca studentul cu ID-ul dat nu exista in lista.
        """
        for i, student in enumerate(self.__studenti):
            if student["id"] == id_student:
                del self.__studenti[i]
                return
        raise ValueError("studentul cu id-ul dat nu exista!")

    def modifica_student(self, student):
        """
        Modifică un student existent în lista de studenți.

        Parametri:
        student (Student): Obiectul student care conține noile date ale studentului.

        Ridică:
        ValueError: Dacă studentul cu ID-ul dat nu există în lista de studenți.
        """
        for i, stud in enumerate(self.__studenti):
            if stud["id"] == student.get_id_student():
                self.__studenti[i] = {"id": student.get_id_student(), "stud": student}
                return
        raise ValueError("studentul cu id-ul dat nu exista!")
    
    def get_student_by_name(self, nume):
        """
        Returnează studentul cu numele dat.

        Args:
            nume (str): Numele studentului cautat.

        Returns:
            Student: Studentul cu numele dat.
        """
        for stud in self.__studenti:
            if stud["stud"].get_nume() == nume:
                return stud["stud"]
        raise ValueError("studentul cu numele dat nu exista!")