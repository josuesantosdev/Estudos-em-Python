
#estudo estrutura condicional - SE. Exemplo
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par")
if numero % 2 != 0:
    print("o número é impar")

#calculo idade
ano_atual = 2025
nascimento = int(input("Digite ano de mascimento: "))
pergunta = input("Você já fez aniversário esse ano?")
resultado = ano_atual - nascimento

if pergunta == "não":
    resultado -= 1  #isso subtrai 1 do valor da var. resultado
    print("sua idade é", resultado)