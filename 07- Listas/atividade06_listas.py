# autor: Hiago Cesar
# projeto: listas em python


nomes = ['Pelé','Maradona', 'Messi', 'Ronaldo']
print('nomes')

# adicionado um nome na lista
# para retirar as aspas e os colchetes, use *
nomes.append('Pedra')
print(*nomes)

# adicionando um nome em uma posição especifica
nomes.insert(4,'neymar')
print(*nomes)

#Modificar uma pessoa da lista
nomes [5] = 'mbappe'
print(*nomes)

# modificar uma pessoa da lista
del nomes [2]
print(*nomes)

# removendo um nome por testo
# buscar o nome e apagar o primeiro que aparecer
nomes.remove('Maradona')
print(*nomes)

#Usando o pop para mostrar o nome removido
#  0      1      2       3 
# Pelé Ronaldo Neymar Mbappe
removido = nomes.pop(1)
print(f'Após o pop foi removido o nome:{removido},nomes')

# limpar a lista
nomes.clear()
print(f'Após o clear a lista é: {nomes}')