pares = []
impares = []
for i in range(5):
    numeros = int(input("Digite um número:"))
    if numeros %2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)
    pares.sort() #exemplo para ordenar lista
    impares.sort() #exemplo para ordenar lsta
print("Pares:", pares, "Impares:", impares)