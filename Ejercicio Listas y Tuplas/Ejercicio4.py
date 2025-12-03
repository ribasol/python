numeros_ganadores = []
print("Por favor, introduce los 6 números ganadores de la lotería primitiva.")

for i in range(6):
    while True:
        try:
            numero = int(input(f"Introduce el número {i+1}: "))
            if 1 <= numero <= 49:
                numeros_ganadores.append(numero)
                break
            else:
                print("Error: El número debe estar entre 1 y 49.")
        except ValueError:
            print("Error: Por favor, introduce un número válido.")

numeros_ganadores.sort()

print("Los números ganadores ordenados son:", numeros_ganadores)
