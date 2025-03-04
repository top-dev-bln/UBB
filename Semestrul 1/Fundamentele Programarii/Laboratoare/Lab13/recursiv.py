def backtrack(pos, expr, result, operators, numbers, solutions):
    if pos == len(numbers) - 1:  # condiția de oprire
        if result > 0:  
            solutions.append("".join(expr))  # este solutie
        return
    
    
    expr.append(f"+{numbers[pos + 1]}")
    backtrack(pos + 1, expr, result + numbers[pos + 1], operators, numbers, solutions)
    expr.pop()  

   
    expr.append(f"-{numbers[pos + 1]}")
    backtrack(pos + 1, expr, result - numbers[pos + 1], operators, numbers, solutions)
    expr.pop()  


def gasire_pozitive(numere):
    if not numere:
        return []

    solutii = []
    start = [str(numere[0])]  
    backtrack(0, start, numere[0], ["+", "-"], numere, solutii)
    return solutii



numere = [3, 2, 1, 4]
solutii = gasire_pozitive(numere)
print("Expresii care au un rezultat pozitiv:")
for solutie in solutii:
    print(solutie)
