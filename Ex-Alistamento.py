ano_nascimento = 2017
ano_atual = 2025
idade = ano_atual - ano_nascimento
referencia = 18
faltam = referencia - idade
excedeu = idade - referencia

if idade == referencia:
    print("Está na hora de se alistar! Você já tem 18 anos, ou completa 18 anos esse ano.")
elif idade < referencia:
    print("Faltam {} anos para você se alistar, você tem {} anos." .format(faltam, idade))
else:
    print("Você não se alista mais. A data para se alistar seria a {} anos atrás, sua idade é {}" .format(excedeu,idade))


