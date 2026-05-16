## Autor> Hiago Cesar
# Projeto: Desvio Condicional

# Criação das variáveis
nome = input("Digite seu nome: ")
nota = float(input("Digite a sua nota: "))
if nota >=7:
    print('Aluno aprovado!')
elif nota <=4 and nota >= 7:
    print('Aluno de recuperação!')
else:
    print('Aluno reprovado!')