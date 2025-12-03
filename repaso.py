altura = int(input("Introduce un numero: "))

espacios = ' '
for fila in range(altura,0,-1):
    print(espacios * fila + "*")
