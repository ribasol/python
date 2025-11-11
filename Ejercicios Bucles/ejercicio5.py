inversion = input("Introduzca cantidad de inversion: ")
interes = int(input("Introduzca interes anual: "))
años = int(input("Introduzca numero de años: "))

for año in range(1, años + 1):
    capital = inversion * (1 + interes / 100)
    print("año", año, ": capital =", round(capital, 2), "€")