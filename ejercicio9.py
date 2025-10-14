cantidad = float(input("Introduzca cantidad a invertir: "))
interes = float(input("Introduzca interes anual: "))
años = float(input("Introduzca numero de años: "))
operacion = cantidad * (1 + interes / 100) ** años

print("Capital obtenido en la inversión: ", round(operacion ,2))
