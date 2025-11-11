#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
contraseña1 = input("Introduzca la contraseña: ")
contraseña = "python123"
while contraseña1 != contraseña:
    contraseña1 = input("Contraseña incorrecta. Introduzca la contraseña: ")