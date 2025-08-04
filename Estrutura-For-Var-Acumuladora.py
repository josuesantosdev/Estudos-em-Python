acumuladora = 0
qtdade = int(input("Quantos números deseja informar?"))
#for i in range(5):
for i in range(qtdade):
    n = int(input("Digite um número:"))
    metade = n / 2
    print(metade)
    acumuladora = acumuladora + metade
print("A soma de todas as metades é", acumuladora)

