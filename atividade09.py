#Autor: Hiago Cesar
#Entrada de imc

nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso')
else:
    print('Peso normal')