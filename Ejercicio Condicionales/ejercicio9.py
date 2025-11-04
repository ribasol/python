edad = int(input("Introduce tu edad: "))

if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 5
else:
    precio = 10

if precio == 0:
    print("Puedes entrar gratis")
else:
    print(f"El precio de la entrada es de {precio} €.")
