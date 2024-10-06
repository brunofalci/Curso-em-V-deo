# Faça um programa que leia o nome completo de uma pessoa,
n = str(input('Digite seu nome completo: ')).strip()
#  mostrando em seguida o primeiro e o 
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome[0].lower().capitalize()))
# último nome separadamente.
print('Seu ultimo nome é: {}'.format(nome[-1].lower().capitalize()))
