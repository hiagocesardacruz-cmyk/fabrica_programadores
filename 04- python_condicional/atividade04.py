 # Autor> Hiago Cesar
# Projeto: Desvio Condicional

# Criação das variáveis
nome = input("Digite seu nome: ")
idade = float(input("Digite sua idade: "))
carteira = input(("Tem carteira de motorista?: "))
if carteira == "sim" and idade >= 18:
    print('Pode dirigir')
else:
    print('Não pode dirigir')