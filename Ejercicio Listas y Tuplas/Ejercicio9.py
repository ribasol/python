palabra = input("Introduce una palabra: ").lower()
vocales = "aeiou"
contador = {}

for v in vocales:
    contador[v] = 0

for letra in palabra:
    if letra in vocales:
        contador[letra] += 1

for v, num in contador.items():
    print(f"La vocal '{v}' aparece {num} veces.")
