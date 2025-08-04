#exercício que calcula porcentagem
salario = 4700
limite = salario * 30 /100 #30 % da renda (salário)
prestacao = 1300 #se 30% do salário for inferior ao valor da parcela, reprovado.

if limite >= prestacao:
    print("Empréstimo aprovado.")

else:
    print("reprovado")

