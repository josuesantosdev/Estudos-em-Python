#algorítimo que recebe os dados, e calcula idade atual a partir do ano de nascimento, ano do primeiro contrato +
# qual idade irá se aposentar.
#que nesse caso é a idade na primeira contribuição + 35

dados = {}
dados["nome"] = input("Digite seu nome")
dados["ano nascimento"] = int(input("Digite o ano do seu nascimento:"))
dados["idade"] = 2025 - dados["ano nascimento"]
dados["CTPS"] = int(input("Digite o número da sua CTPS:"))
dados["Salário"] = float(input("Digite o seu salário:"))
dados["contratação"] = int(input("Digite o ano da sua contratação:"))
dados["aposentadoria"] = dados["contratação"] - dados["ano nascimento"] + 35

print(dados)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
