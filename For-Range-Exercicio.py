#Elabore um programa que solicite ao usuário dez números e efetue a soma, exibindo o resultado. /
# Contudo, se em algum momento o número digitado for 0, deve interromper o laço, mostrando a soma /
# apenas dos valores informados até então.

soma = 0

for i in range(10):
    num = int(input("Digite o " + str(i+1) + " Número: "))
    if num == 0:
        print("Não é permitido 0")
        break
    soma += num
print(soma)


