def validare_data(ziua:int,luna:int,anul:int):
    if ziua < 1 or ziua > 31:
       raise ValueError("Ziua invalida")
    if luna < 1 or luna > 12:
     raise ValueError("Luna invalida")
    if anul < 1:
     raise ValueError("Anul invalid")
 
def validare_pret(price:float):
    if price <= 0:
      raise ValueError