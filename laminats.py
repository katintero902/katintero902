
import math


def linoleja_izmaksas(cena, l_platums, i_garums, i_platums):
    
    r_platums = math.ceil(i_platums)
    r_garums = math.ceil(i_garums)

    i_laukums = r_platums * r_garums
    
    linolejs = i_laukums / l_platums

    result = linolejs * cena

    return round(result, 2)



cena = float(input("Ievadiet linoleja cenu EUR/m²: "))

l_platums = float(input("Ievadiet linoleja platumu m: "))

i_garums = float(input("Ievadiet istabas garumu m: "))
i_platums = float(input("Ievadiet istabas platumu m: "))

summa = linoleja_izmaksas(cena, l_platums, i_garums, i_platums)


print(f"Linoleja ieklāšanas izmaksas: {summa: .2f} EUR")
