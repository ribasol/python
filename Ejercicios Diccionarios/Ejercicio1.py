dic = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

pregunta = input("Di una divisa: ")

# Convertimos la entrada a formato con primera letra mayúscula
clave = pregunta.capitalize()  

if clave in dic:
    print("Su símbolo es:", dic[clave])
else:
    print("La divisa no está en el diccionario.")
