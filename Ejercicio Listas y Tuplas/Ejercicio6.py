asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
repetir = []  # aquí guardamos solo las suspensas

for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    if nota < 5:
        repetir.append(asignatura)

print("\nAsignaturas que tienes que repetir:")
for asignatura in repetir:
    print(asignatura)
