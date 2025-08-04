# Elabore um programa que solicite ao usuário 5 números e efetue a multiplicação, exibindo /
# o resultado. No entanto, se em algum momento o número digitado for 0, deve pular esta iteração, /
# para que o valor não seja zerado.

multiplicacao = 1
for i in range(5):
    num = int(input("Digite os valores"))
    if num == 0:
        continue
    multiplicacao *= num
print(multiplicacao)
