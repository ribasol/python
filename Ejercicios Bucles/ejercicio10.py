#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
numero = int(input("Introduzca un número entero: "))
es_primo = True
for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        break
    
if es_primo and numero > 1:
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")
