#Autor: Hiago Cesar
#Projeto: Trabalhando com arquivos

nome = input('Digite o seu nome:')
email = input('Digite seu email:')
número = input('Digite o seu número:')

arquivo = open('pessoa.txt' , 'a')
arquivo.write(nome+ " | " + email + '|' + número + '\n')
arquivo.close