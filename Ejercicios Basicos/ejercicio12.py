barras_no_frescas = int(input("Introduce el número de barras vendidas que no son del día: "))

precio_barra = 3.49
descuento = 0.60

precio_descuento = precio_barra * (1 - descuento)
coste_total = barras_no_frescas * precio_descuento

print(f"Precio habitual de una barra de pan: {precio_barra:.2f} €")
print(f"Descuento por no ser fresca: {descuento * 100:.0f}%")
print(f"Coste total a pagar: {coste_total:.2f} €")
