tipo = input("¿Quieres una pizza vegetariana? (sí/no): ")

if tipo.lower() == "sí" or tipo.lower() == "si":
    print("Ingredientes vegetarianos: pimiento y tofu")
    ingrediente = input("Elige un ingrediente: ")
    print(f"Tu pizza es vegetariana y lleva mozzarella, tomate y {ingrediente}.")

else:
    print("Ingredientes no vegetarianos: peperoni, jamón y salmón")
    ingrediente = input("Elige un ingrediente: ")
    print(f"Tu pizza no es vegetariana y lleva mozzarella, tomate y {ingrediente}.")
