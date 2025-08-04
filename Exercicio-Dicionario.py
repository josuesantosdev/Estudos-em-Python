#Elabore um programa que simule o cadastro de telefones com dicionário como uma agenda, /
# exibindo, ao final, o dicionário.

agenda = {}
print("Cadastro de Telefones")
while True:
    contato = input("Digite o nome do Contato:")
    telefone = input("Digite o número do contato:")
    agenda[contato] = telefone #Adicionamos o telefone no dicionário agenda./
    # A chave para encontrarmos o telefone será o contato.
    if input("Deseja continuar: s/n ?") == "n":
        break
print(agenda)

