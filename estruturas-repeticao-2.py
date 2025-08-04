#Elabore um programa que solicite três números, some-os e exiba o resultado para o usuário.

soma = 0
for var in range (3):
    num = int(input("Digite um número:"))
    soma += num
print(soma)
#se estivesse alinhado ao bloco de ação, iria mostrar todas as somas separadas, assim mostra o total

for i in range (5):
    print(i)

for a in range (2, 7):
    print(a)

for b in range (4,12, 2): #4 incio, 12 fim, 2 passo: vai contar de 2 e 2.
    print (b)

for c in range (5,0,-1): #sequência decrescente gerará os números 5, 4, 3, 2 e 1, nesta ordem
    print(c)