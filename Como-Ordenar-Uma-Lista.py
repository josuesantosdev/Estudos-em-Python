#algorítimo de ordenação
nums = [17, 33, 23, 11, 8, 15, 9]
aux = 0
for _ in range(len(nums) - 1): #se a variável contadora não for utilizada dentro do bloco de /
    # códigos do laço, não será necessário declará-la, fazendo uso do símbolo de underscore (_).
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            aux = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = aux
print(nums)



