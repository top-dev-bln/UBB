def test_gasire_pozitive():
    numere = [3, 2, 1, 4]
    solutii = gasit_pozitive_iterativ(numere)
    print("Expresii care au un rezultat pozitiv:")


    assert len(solutii) <= 2**(len(numere) - 1)
    assert "3+2+1+4" in solutii
    assert "3-2+1+4" in solutii
    assert "3+2-1+4" in solutii
    assert "3-2-1+4" in solutii
    assert "3+2+1-4" in solutii

    assert "3-2-1-4" not in solutii

    print ("Testele trecute cu succes!")



def consistent_iterative(result, remaining_sum):
    return result + remaining_sum > 0

def solution_iterative(result):
    return result > 0

def gasit_pozitive_iterativ(numere):
    if not numere:
        return []

    n = len(numere)
    solutii = []
    combinatii = 2 ** (n - 1)

    for i in range(combinatii):
        expr = str(numere[0])  
        rezultat = numere[0]

        for j in range(n - 1):
            if (i // (2 ** j)) % 2 == 0:
                operator = "+"
            else:
                operator = "-"

            if operator == "+":
                rezultat += numere[j + 1]
            else:
                rezultat -= numere[j + 1]
            expr += operator + str(numere[j + 1])

        remaining_sum = sum(numere[j+1:])
        if consistent_iterative(rezultat, remaining_sum) and solution_iterative(rezultat):
            solutii.append(expr)

    return solutii

def run():
    test_gasire_pozitive()
    numere = []
    n = int(input("Dati numarul de numere: "))
    for i in range(n):
        numere.append(int(input("Dati numarul: ")))

    
    solutii = gasit_pozitive_iterativ(numere)
    print("Expresii care au un rezultat pozitiv:")
    for solutie in solutii:
        print(solutie)


run()