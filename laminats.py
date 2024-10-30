
import math


def laminata_izmaksas(cena, laminata_platums, istabas_garums, laminata_platums):
    
    round_platums = math.ceil(istabas_platums)
    round_garums = math.ceil(istabas_garums)

    istabas_laukums = r_platums * r_garums
    
    linolejs = istabas_laukums / l_platums

    result = laminata * cena

    return round(result, 2)



cena = float(input("Ievadiet laminata cenu EUR/m²: "))

laminata_platums = float(input("Ievadiet laminata platumu m: "))

istabas_garums = float(input("Ievadiet istabas garumu m: "))
istabas_platums = float(input("Ievadiet istabas platumu m: "))

summa = laminata_izmaksas(cena, laminata_platums, istabas_garums, istabas_platums)


print(f"laminata ieklāšanas izmaksas: {summa: .2f} EUR")
