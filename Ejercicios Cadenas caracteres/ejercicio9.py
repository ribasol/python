#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
#dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
#anterior para que también funcione cuando el día o el mes se introduzcan con un
#solo carácter.

fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
partes = fecha.split("/")

dia = partes[0].zfill(2)
mes = partes[1].zfill(2)
año = partes[2]

print("Día:", dia)
print("Mes:", mes)
print("Año:", año)
