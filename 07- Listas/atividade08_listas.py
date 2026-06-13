# autor: Hiago Cesar
# projeto: listas em python

nome = input("Digite o seu nome para incluir na agenda: ")

nomes = ['steffanie','josé', 'enzo', 'patricia']
print('nomes')

nomes.append('Pedra')
print(*nomes)

del nomes[3]
print(*nomes)
 
removido = nomes.pop(1)
print(f'Após o pop foi removido o nome:{removido}')