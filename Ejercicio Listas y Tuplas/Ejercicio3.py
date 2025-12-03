asignaturas = ['Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lengua']
notas = []

for i in asignaturas:
    nota = float(input(f"Introduzca su nota para {i}: "))
    notas.append(nota)

asignaturas_repetir = []

x = 0
while x < len(asignaturas):
    if notas[x] < 5:
        asignaturas_repetir.append(asignaturas[x])
        x += 1
print(f"Las asignaturas que tienes que repetir son: {asignaturas_repetir}")
