#variáveis com solicitações das notas do usuário
nota_1 = float(input("Digite a primeira nota:"))
nota_2 = float(input("Digite a segunda nota:"))
nota_3 = float(input("Digite a terceira nota:"))
nota_4 = float(input("Digite a quarta nota:"))

#calcula a média das notas
media = (nota_1 + nota_2 + nota_3 + nota_4) /4

#verifica se o estudante foi aprovado
if media >= 7:
    print("Você foi aprovado")
    print("ainda estamos dentro do if")
if media < 7:
    print("Você foi reprovado")

#exibe a média - Saímos do if no caso de a nota ser menor que 7 (reprovação) ele só mostraria esse print
print(f"A média é: {media:.2f}")
