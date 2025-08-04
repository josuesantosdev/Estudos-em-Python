def imc (p,a):
    r = p / (a**2)
    print(f'Seu IMC é {r:.2f}')

imc(75,1.85)


def imc_lista (lista):
    for pessoa in lista:
        altura = pessoa ["altura"]
        peso = pessoa ["peso"]
        imc = peso / (altura**2)
        print(f'O imc de {pessoa["nome"]} é de {imc:.2f}')

pessoa = [
    {"nome" : "Josué", "peso" : 75, "altura": 1.85},
    {"nome" : "Marisa", "peso" : 79, "altura": 1.64},
    {"nome" : "Carla", "peso" : 65, "altura": 1.65}
]

imc_lista(pessoa)


pessoa2 = [
    {"nome" : "Julio", "peso" : 82, "altura": 1.83},
    {"nome" : "Maria", "peso" : 74, "altura": 1.64},
    {"nome" : "Tamy", "peso" : 66, "altura": 1.65}
]

imc_lista(pessoa2)