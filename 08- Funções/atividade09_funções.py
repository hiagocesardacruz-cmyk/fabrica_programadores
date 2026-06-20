# Autor> Hiago Cesar
# Projeto: Desvio Condicional

# Criação das variáveis
nome = input("Digite seu nome: ")
idade = float(input("Digite sua idade: "))
carteira = input("Tem carteira de motorista?: ")


def pode_dirigir(idade, carteira):
    carteira_norm = carteira.strip().lower()

    if carteira_norm == "sim" and idade >= 18:
        print('Pode dirigir')
    else:
        print('Não pode dirigir')


# chamada da função
pode_dirigir(idade, carteira)

