numero = int(input("Digite um número: "))

try:

    print(numero / 0.0)

except:

    print("Não foi possível dividir o número por zero.")


#exercício
while True:

    print("1. Doces")

    print("2. Salgados")

    print("3. Bebidas")

    print("4. Sair")

    try:

        opcao = int(input("Digite uma opção:"))

    except:

        print("Você digitou uma opção inválida. Tente novamente.")

        continue

    if opcao >= 1 and opcao <= 3:

        print(f"Você digitou a opção válida \"{opcao}\".")

    elif opcao == 4:

        break

    else:

        print("Você digitou uma opção inválida. Tente novamente.")