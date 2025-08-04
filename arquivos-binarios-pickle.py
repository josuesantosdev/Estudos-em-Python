# Salve uma lista de números inteiros em um arquivo chamado “dados.pickle”.

import pickle

dados = [1,2,3,4,5,6,11,17,23]
#wb: escrever binário - Write Binary
with open("dados.pickle", "wb") as arquivo:
    pickle.dump(dados,arquivo)

import pickle


with open("dados.pickle", "rb") as arquivo: #rb = read binary
    ler = pickle.load(arquivo)
    print(ler)




