creditos = {
    "Matemáticas": 6,
    "Física": 4,
    "Química": 5
}

total = 0

for asignatura, creditos_asig in creditos.items():
    print(f"{asignatura} tiene {creditos_asig} créditos")
    total += creditos_asig

print("Total de créditos del curso:", total)
