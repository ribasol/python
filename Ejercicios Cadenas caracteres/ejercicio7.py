#Escribir un programa que pregunte el correo electrónico del usuario en la consola y
#muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante
#de la arroba @) pero con dominio ceu.es.

correo = input("Introduce tu correo electrónico: ")
nombre = correo.split("@")[0]
nuevo_correo = nombre + "@ceu.es"

print("Tu nuevo correo es:", nuevo_correo)
