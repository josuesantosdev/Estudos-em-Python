#jeito não dinâmico - pré definido
nums = [0,0,0,0,0]
for i in range(5):
    num = int(input("Digite um número:"))
    nums [i] = num
print (nums)

#jeito dinâmico
nums = []
for i in range(5):
    num = int(input("Digite um número:"))
    nums.append(num)
print(nums)


