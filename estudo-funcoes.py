import json

arquivo_json = "teste_alunos2.json"

#FUNÇÃO PERSISTÊNCIA - JSON
def salvar (lista):
    with open (arquivo_json, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)


#FUNÇÃO PERSISTÊNCIA - JSON
def ler ():
    try:
        with open (arquivo_json, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

#FUNÇÃO INCLUSÃO
def incluir (lista):
    print("Estudantes - Incluir")
    try:
        codigo_inclusao = int(input("Digite o código:"))
    except ValueError:
        print("Valor inválido")
        return

    for estudante in lista:
        if estudante ["codigo"] == codigo_inclusao:
            print("Esse aluno já existe!")
            return

    nome = input("Digite o nome:")
    cpf = int (input("Digite o CPF:"))

    dicionario_estudante = { "codigo": codigo_inclusao, "nome": nome, "cpf": cpf }

    lista.append(dicionario_estudante)
    salvar(lista)

    print ("Aluno incluído com sucesso!")

#FUNÇÃO LISTAGEM
def listar (lista):
    if not lista:
        print("A lista está vazia")
    else:
        for item in lista:
            print(item)
    return


#funcao editar
def editar(lista):
    print("Estudantes - editar")
    try:
        codigo_editar = int(input("Digite o código:"))
    except ValueError:
        print("Valor inválido")
        return

    for a in lista:
        if a["codigo"] == codigo_editar:
            print(f'Aluno(a) de código: {a["codigo"]}, nome: {a["nome"]} e CPF: {a["cpf"]} localizado(a).')
            nome = input("Digite o novo nome:")
            cpf = int(input("Digite o novo CPF:"))

            a["nome"] = nome
            a["cpf"] = cpf

            salvar(lista)
            print("Aluno editado com sucesso!")

        else:
            print("Aluno não localizado.")


def excluir(lista):
    print("Estudantes - excluir")
    try:
        codigo_excluir = int(input("Digite o código:"))
    except ValueError:
        print("Valor inválido")
        return

    for a in lista:
        if a["codigo"] == codigo_excluir:
            print("Aluno localizado.")
            print("Código:", a["codigo"], "nome:", a["nome"], "CPF:", a["cpf"])
            confirmar = input("Tem certeza que deseja excluir? s/n:") .lower()
            if confirmar == "s":
                lista.remove(a)
                salvar(lista)
                print("Aluno excluído com sucesso!")
        return

    else:
        print("Aluno não localizado.")



def exibir_main ():
    print("----MENU PRINCIPAL----")
    print("1 - Alunos")
    print("2 - Professores")
    print("6 - Sair")
    return int(input("Digite a opção desejada:"))

def operacoes ():
    print(f"----ESTUDANTES----")
    print("1 - Incluir")
    print("2 - Listar")
    print("3 - Editar")
    print("4 - Excluir")
    print("5 - Voltar ao menu principal")
    return int(input("Digite a opção desejada:"))

def gerenciamento (lista):
    while True:
        try:
            opcao = operacoes()
            if opcao == 1:
                incluir(lista)

            elif opcao == 2:
                listar(lista)

            elif opcao == 3:
                editar(lista)

            elif opcao == 4:
                excluir(lista)

            elif opcao == 5:
                break

            else:
                print("Opção inválida")

        except ValueError:
            print("Opção inválida")

#main
def main ():

    lista = ler()

    while True:
        try:
            opcao = exibir_main()
            if opcao == 1:
                gerenciamento(lista)

            elif opcao == 6:
                print("Encerrando...")
                break
            else:
                print("Opção inválida")
        except ValueError:
            print("Opção inválida. Tente novamente")

main()




