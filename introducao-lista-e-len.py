#exemplo básico de lista e uso do comando len
#percorra uma lista de animais e mostre os que tem menos de 7 letras

lista = ["Gato", "Cachorro", "Elefante", "Cavalo", "Rinoceronte", "boi"]
for animal in lista:
    tamanho = len(animal) #contador de caracteres
    if tamanho < 7:
        print (animal)