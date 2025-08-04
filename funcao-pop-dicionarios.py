agenda = {"Maria": "(41) 98765-4321", "João": "(11) 12345-6789"}
print(agenda.pop("Maria", "Contato com nome Maria localizado")) #remove maria
print(agenda.pop("José", "Contato com nome José não localizado"))
if "Josué" in agenda: #consultar
    print("Josué está na agenda")
else:
    print("Josué não está na agenda")
print(agenda)

#del agenda["Maria"] remover, mas dá erro se não tiver na lista. Verificar antes