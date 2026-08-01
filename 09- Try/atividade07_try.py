#Autor: Hiago Cesar

# Autor: Nilton barros
# Projeto: Loop For - variaveis de loop 

numero = 2
# loop FOR
        
        
try:
    numero = int(input('Digite a tabuada que deseja :'))
    numero_inicio = int(input(' Digite o inicio da tabuda :'))
    numero_fim = int(input('Digite o fim da tabuada:'))

    for i in range (numero_inicio, numero_fim + 1):
         print(f'{ numero} x {i} = { 1 * numero}')

except:
     print("Ocorreu um erro na operação:")