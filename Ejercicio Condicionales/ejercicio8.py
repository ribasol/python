puntuacion = float(input("Introduce tu puntuación (0.0, 0.4, 0.6 o más): "))

dinero_base = 2400

if puntuacion == 0.0:
    nivel = "Inaceptable"
elif puntuacion == 0.4:
    nivel = "Aceptable"
elif puntuacion >= 0.6:
    nivel = "Meritorio"
else:
    nivel = None

if nivel is None:
    print("Error: la puntuación introducida no es válida.")
else:
    dinero = dinero_base * puntuacion
    print(f"Tu nivel de rendimiento es {nivel}.")
    print(f"Recibirás {dinero:.2f} €.")