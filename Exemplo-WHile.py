#faça um algorítimo que lime a quantidade de cupons de desconto de um restaurante.
#no máximo 10 por noite, ir avisando quantos ainda restam e avisar quando chegar no limete que é 10

limite = 10
while limite > 0:
    #while true - essa seria uma forma para não ser um loop infinito, colocando break no fim
    quantidade = int(input("Quantos limites foram apresentados?"))
    limite = limite - quantidade
    if limite > 0:
        print ("Ainda temos {} cupons" .format(limite))
    else:
        print("Não temos mais cupons")
        #break - ex break, quebra a execução