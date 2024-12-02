class ValidatorStudent:

    def valideaza_student(self,student):
        erori = ""
        if student.get_id_student() <0:
            erori+= "id student invalid!"
        if student.get_nume() == "":
            erori+= "nume student invalid!"

        if len(erori)>0:
            raise ValueError(erori)
