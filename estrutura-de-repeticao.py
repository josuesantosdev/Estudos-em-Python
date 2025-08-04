#estruturas de repetição
#crie um algorítimo que peça 5 números para o usuário, mostre a metade dos números e apresente a soma das /
#metades no final

#para declarar uma variável somatória ou acumuladora, declare ela antes do bloco de execução
soma_metades = 0 #começa com 0

#este exemplo é quando já se tem um número fixo de repetições
for n in range (5): #precisa ser criada uma variável
    n = float(input("Digite um valor:"))
    metade = n / 2
    print (metade)
    soma_metades = soma_metades + metade #tem que ser assim para pegar todos os valores - não sobrepor
print (soma_metades)

#exemplo sem uma quantidade pré definida

soma_metades = 0 #começa com 0
qtdade = int(input("Quantos números você quer digitar?"))

for n in range (qtdade):
    n = float(input("Digite um valor:"))
    metade = n / 2
    print (metade)
    soma_metades = soma_metades + metade
print (soma_metades)

