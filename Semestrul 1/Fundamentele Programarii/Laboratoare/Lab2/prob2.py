from datetime import datetime


def valoare_valida(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Valoarea trebuie să fie un număr pozitiv.")
        except ValueError:
            print("Te rog introdu un număr valid.")

print("spune-mi cand te-ai nascut: ")

your_year = valoare_valida("Anul: ")
your_month = valoare_valida("Luna: ")
your_day = valoare_valida("Ziua: ")

today = datetime.today()

birth = datetime(your_year, your_month, your_day)

zile = (today - birth).days

print("ai trait " + str(zile) + " zile")
