class ValidatorLaborator:

    def valideaza_laborator(self,laborator):
        erori = ""
        if laborator.get_numar_laborator() <0:
            erori+= "numar laborator invalid!"
        if laborator.get_numar_problema() <0:
            erori+= "numar problema invalid!"
        if laborator.get_descriere() == "": 
            erori+= "descriere invalid !"
        deadline = laborator.get_deadline()
        if deadline.month < 1 or deadline.month > 12:
            erori+= "luna invalida!"
        if deadline.day < 1 or deadline.day > 31:
            erori+= "zi invalida!"



        if len(erori)>0:
            raise ValueError(erori)
