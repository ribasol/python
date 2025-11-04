nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M para mujer, H para hombre): ")

nombre = nombre.capitalize()
sexo = sexo.upper()

if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    print("Perteneces al grupo A.")
else:
    print("Perteneces al grupo B.")