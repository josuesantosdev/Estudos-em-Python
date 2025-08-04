num = 6/7
outro_num = 10
t1 = "hello"
t2 = "World"

print(f'Resultado: {num:f}')
print(f'Resultado: {num:.2f}')
print(f'Resultado: {num:8.2f}')
print(f'Resultado: {outro_num:8d}')
print(f'Resultado: {outro_num:d}')
print (f'{t1}{t2}')
print (f'{t1:10}{t2:10}')  #formato com no mínimo 10 caracteres sem alinhamento
print (f'{t1:^10}{t2:^10}')  #formato com no mínimo 10 caracteres centralizado
print (f'{t1:>10} {t2:>10}')  #formato com no mínimo 10 caracteres a direita
