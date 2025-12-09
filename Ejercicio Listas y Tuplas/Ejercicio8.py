palabra = input("Introduce una palabra: ")

p = palabra.lower()

if p == p[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
