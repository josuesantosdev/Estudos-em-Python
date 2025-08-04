with open("dados.txt", "w") as arquivo: #tem que ter with para fechar corretamente o arquivo

  arquivo.write("Counter-Strike é melhor do que Valorant.")

  arquivo.write("O correto é 'bolacha'.")


with open("dados.txt", "a") as arquivo: #A Apend. Adiciona no fim do arquivo sem apagar.
  arquivo.write("Testando")

with open("dados.txt", "r") as arquivo:
  linhas = arquivo.readlines()
  print(linhas)
