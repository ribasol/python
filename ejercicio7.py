kilos = float(input("Introduzca su peso: "))
metros = float(input("Introduzca su estatura: "))
masa_corporal = kilos / (metros ** 2)

print("Tu indice de masa corporal es de: ", round(masa_corporal, 2))
