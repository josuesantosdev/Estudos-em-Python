import json

arquivo_alunos = "novos_estudantes.json"


#persistência json
def salvar_arquivo(lista_alunos):
    with open (arquivo_alunos, "w", encoding="utf-8") as f:
        json.dump(lista_alunos, f, ensure_ascii=False, indent=4)


#persistência json
def ler():
    try:
        with open (arquivo_alunos, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def incluir (lista_alunos):
    print("----Estudantes----Incluir")
    try:
        codigo = int(input("Informe o código do estudante: "))
    except ValueError:
        print("Valor inválido, tente novamente")
        return

    for estudante in lista_alunos:
        if estudante["codigo"] == codigo:
            print("Aluno já existe.")
            return


    nome = input("Informe o nome do estudante: ")
    cpf = input("Informe o CPF do estudante: ")
    estudante = {"codigo": codigo, "nome": nome, "CPF": cpf}

    lista_alunos.append(estudante)
    salvar_arquivo(lista_alunos)

    print("Aluno incluído com sucesso.")


def listar (lista_alunos):
    print("----Estudantes----Listar")
    if not lista_alunos:
        print("A lista está vazia.")
    else:
        for aluno in lista_alunos:
            print(aluno)


def exibir_menu_principal ():

    print("-" * 30)
    print("Menu Principal")
    print("-" * 30)
    print("1 - Estudantes\n"
          "2 - Professores\n"
          "3 - Disciplinas\n"
          "4 - Turmas\n"
          "5 - Gerenciar Matrículas\n"
          "6 - Sair")
    return int(input("Digite a opção desejada:"))



def submenu():

    print("-" * 30)
    print("Menu Estudantes")
    print("-" * 30)
    print("1 - Incluir")
    print("2 - Listar")
    print("5 - Voltar ao menu principal")
    return int(input("Digite a opção desejada:"))




def gerenciar_itens(lista_alunos):

    try:
        while True:
            opcao = submenu()
            if opcao == 1:
                incluir(lista_alunos)
            elif opcao == 2:
                listar(lista_alunos)
            elif opcao == 5:
                break
            else:
                print("Opção inválida. Tente novamente.")
        return
    except ValueError:
        print("valor inválido")


def main ():
    lista_alunos = ler()

    while True:
        try:
            opcao = exibir_menu_principal()
            if opcao == 1:
                gerenciar_itens(lista_alunos)
            elif opcao == 6:
                print("Encerrando o programa. Até mais..")
                break
            else:
                print("Opção inválida. Tente novamente")
        except ValueError:
            print("Opção inválida. Tente de novo")

main()












