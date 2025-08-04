#Elabore um programa que solicite ao usuário que digite indefinidamente números e efetue a soma, /
# parando apenas quando o usuário digitar o número 0.

soma = 0
num = -1
while num != 0:
    num = int(input("Digite um valor:"))
    soma += num
print(soma) #só mostra o resultado quando digitar 0

soma1 = 0
num1 = -1
while True:
    num1 = int(input("Digite um valor"))
    if num1 == 0:
        break
    soma1 += num1
print(soma1)
