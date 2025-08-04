# Elabore um programa que solicite ao usuário cinco números e exiba duas listas separadas: /
# uma contendo somente números pares e outra contendo somente números ímpares.

pares = []
impares = []
for i in range(5):
    num = int(input("Digite um valor:"))
    if num %2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("Numeros pares", pares, "Números ímpares", impares)

#Acessando dados em uma lista
numbers = [1,3,5,11,7,8]
for i2 in range(len(numbers)): #função len permite saber o comprimento - tamanho de uma lista
    print(numbers[i2])

#Também podemos acessar os elementos pelo índice relativo. No exemplo acima, nums[-1] permitiria acessar /
# o último elemento da lista. Já nums[-2] permitiria acessar o penúltimo elemento, nums[-3] permitiria /
# acessar o antepenúltimo elemento, e assim sucessivamente.

