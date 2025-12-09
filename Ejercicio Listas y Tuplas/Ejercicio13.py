import math

entrada = input("Introduce los números separados por comas: ")
numeros = [float(n) for n in entrada.split(",")]

media = sum(numeros) / len(numeros)

suma_cuadrados = sum((x - media) ** 2 for x in numeros)
desviacion = math.sqrt(suma_cuadrados / len(numeros))

print(f"Media: {media}")
print(f"Desviación típica: {desviacion}")
