#Autor: Hiago Cesar
# Autor: Hiago Cesar

try:
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")

except :
    print("Ocorreu um erro na operação:")