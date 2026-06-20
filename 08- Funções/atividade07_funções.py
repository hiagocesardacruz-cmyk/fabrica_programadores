#Autor: Hiago Cesar
#Entrada de imc

peso = float(input('Digite seu peso em kg:'))
altura = float(input('Digite sua altura (ex: 1.75): '))

def calcular(peso, altura):
    if altura == 0:
        print('A altura não pode ser 0.')
        return

    imc = peso / (altura * altura)
    print(f'O resultado do seu IMC é: {imc:.2f}')

# chamada da função
calcular(peso, altura)

