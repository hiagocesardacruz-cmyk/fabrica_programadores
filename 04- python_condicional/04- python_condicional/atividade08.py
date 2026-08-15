## Autor> Hiago Cesar
# Projeto: Desvio Condicional

# Criação das variáveis
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
resultado = salario * 0.10
if resultado > 100:
    print("Você tem dinheiro!")
else:
    print("Você é pobre!")