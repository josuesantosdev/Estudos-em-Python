import json #Nesta linha, estamos importando o módulo json da biblioteca padrão do Python
dados = {
  "nome": "Josué",
  "idade": "32",
  "cidade": "curitiba",
  "frutas favoritas": [
    "banana", "abacate", "uva"
  ]
}

#encoding: para garantir que caracteres especiais (como o “ã” e “ç”) sejam tratados corretamente.
with open("pessoa.json", "w", encoding="utf-8") as arquivo:
  json.dump(dados, arquivo, ensure_ascii=False)
  #permitir a codificação correta de caracteres não-ASCII (isto é, caracteres que não façam parte \
  # do alfabeto da língua inglesa).

#lendo
with open("pessoa.json", "r", encoding="utf-8") as arquivo:
  dados_lidos = json.load(arquivo)
  print(dados_lidos)

for i in dados.items():
  print(i)


