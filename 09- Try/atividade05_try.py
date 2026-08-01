#Autor: Hiago Cesar
#Projeto: entendendo tratamento de exceção

try:
    dolar = 5.08
    real = float(input("Digite o valor em reais (R$): "))
    conversao = real / dolar

    print(f"Valor em dólares: US$ {conversao:.2f}")

except:
    print("Ocorreu um erro na operação:")