#saber o menor e maior e a posição(índice)
lista = [11,10,7,22,17]
maior = lista[0]
menor = lista[0]
posicao_maior = 0
posicao_menor = 0

for p, n in(enumerate(lista)):

    if n < menor:
        menor = n
        posicao_menor = p

    if n > maior:
        maior = n
        posicao_maior = p

print(f'O maior é {maior} na posição {posicao_maior} e o menor é {menor} na posição {posicao_menor}')
