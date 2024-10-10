def data_calendaristica(an, zi_de_an):
    
  
    
    luna = 0
    while zi_de_an > zile_luni[luna]:
        zi_de_an -= zile_luni[luna]
        luna += 1
        

    return an, luna + 1, zi_de_an  # luna + 1 pentru a începe de la 1




an=int(input("Anul: "))
luna=0
zi=int(input("Ziua: "))

if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
    zile_luni = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # an bisect
else:
    zile_luni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # an normal

while zi > zile_luni[luna]:
    zi -= zile_luni[luna]
    luna += 1

print("data este " + str(an) + "/" + str(luna + 1) + "/" + str(zi))