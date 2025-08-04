def calcular_preco(tipo):
    if tipo == 'estudante':
        return 10
    elif tipo == 'comum':
        return 20
    else:
        print("Tipo de ingresso inválido!")
        return 0


capacidade_maxima = 100
ingressos_vendidos = 0

while ingressos_vendidos < capacidade_maxima:
    print(f"Já foram vendidos {ingressos_vendidos} ingressos.")
    ingressos_disponiveis = capacidade_maxima - ingressos_vendidos
    print(f"Ainda temos {ingressos_disponiveis} ingressos disponíveis.")

    try:
        quantidade = int(input("Quantos ingressos você deseja comprar? "))
    except ValueError:
        print("Valor inválido")
        continue

    if quantidade > ingressos_disponiveis:
        print("Desculpe, não temos essa quantidade de ingressos disponíveis.")
        continue

    tipo = input("Qual o tipo de ingresso? (comum/estudante) ")

    total_a_pagar = 0
    for _ in range(quantidade):
        total_a_pagar += calcular_preco(tipo)

    if total_a_pagar > 0:
        print(f"O total a pagar é: R${total_a_pagar}")
        confirmacao = input("Deseja confirmar a compra? (sim/nao) ")

        if confirmacao == 'sim':
            ingressos_vendidos += quantidade
            print("Compra efetuada com sucesso!")
        else:
            print("Compra cancelada.")
    else:
        print("Erro ao processar a compra.")

print("Todos os ingressos foram vendidos! Obrigado!")