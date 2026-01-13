frutas={
    "platano":1.35,
    "manzana": 0.80,
    "pera": 0.85,
    "naranja": 0.70
}

nFruta=input("Dime una fruta: ")
kgFruta=int(input("Cuantos kilos quieres: "))

if nFruta in frutas:
    print(f"El total son {kgFruta*frutas[nFruta]} €")
else:
    print("No tenemos esa fruta")    