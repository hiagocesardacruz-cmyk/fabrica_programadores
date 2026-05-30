#Autor: Hiago Cesar
#Projeto: Loop while


numero = int(input('Digite a tabuada deseja: '))
numero_inicio = int(input('Digite o primeiro valor da tabuada:'))
numero_fim = int(input('Digite o fim da tabuada:'))

while numero_inicio <= numero_fim:
 print(f'{numero} x {numero_inicio} = (numero * numero_incio)')
numero_inicio = numero_inicio + 1