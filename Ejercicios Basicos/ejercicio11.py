balance = float(input("Introduce la cantidad depositada en la cuenta de ahorros: "))

interes = 4

balance_1 = round(balance * (1 + interes / 100), 2)
balance_2 = round(balance_1 * (1 + interes / 100), 2)
balance_3 = round(balance_2 * (1 + interes / 100), 2)

print(f"Tras el primer año: {balance_1} €")
print(f"Tras el segundo año: {balance_2} €")
print(f"Tras el tercer año: {balance_3} €")
