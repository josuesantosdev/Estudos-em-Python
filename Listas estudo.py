#Elabore um programa que solicite ao usuário cinco números, armazene-os em uma lista e exiba como /
# resultado os dados obtidos.

nums = [0,0,0,0,0]
for i in range(5):
    num = int(input("Digite os valores:"))
    nums[i] = num
print (nums)

#exemplo quando se tem uma quantidade pré estabelecida

#abaixo de forma  dinâmica com o método append - que serve para acrescentar itens em uma lista#

nums2 = []
for i2 in range(8):
    num2 = int(input("Digite um valor:"))
    nums2.append(num2)
print(nums2)

#mesmo se eu mudar a quantidade no range ele não dá erro

#Exemplo para acrescentar itens em uma lista

lista = [1,2,3]
lista.append([4,5,6])
print(lista)

lista = [1,2,3]
lista.extend([4,5,6])
print(lista)

nums = [1, 4, 23, 11, 8] #jeito de acessar elementos de uma lista
for i in range(len(nums)):
    print(nums[i])

nums = [1, 4, 23, 11, 8] #jeito simples de acessar toda a lista
for num in nums:
    print(num)

