def gasit_pozitive_iterativ(numere):
    if not numere:
        return []

    n = len(numere)

    solutii = []

    combinatii = 2 ** (n - 1)

    for i in range(combinatii):
        expr = str(numere[0])  
        result = numere[0]

        
        for j in range(n - 1):
            operator = "+" if (i // (2 ** j)) % 2 == 0 else "-"  
            if operator == "+":
                result += numere[j + 1]
            else:
                result -= numere[j + 1]
            expr += operator + str(numere[j + 1])

        
        if result > 0:
            solutii.append(expr)

    return solutii


# Exemplu de utilizare
numere = [3, 2, 1, 4]
solutii = gasit_pozitive_iterativ(numere)
print("Expresii care au un rezultat pozitiv:")
for solutie in solutii:
    print(solutie)
