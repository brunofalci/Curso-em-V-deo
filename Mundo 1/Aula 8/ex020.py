from random import shuffle #embaralha uma lista

a1 = str(input('Nome do 1 aluno: '))
a2 = str(input('Nome do 2 aluno: '))
a3 = str(input('Nome do 3 aluno: '))
a4 = str(input('Nome do 4 aluno: '))

lista = [a1, a2, a3, a4]
shuffle(lista)

print(f'A ordem do sorteio é: {lista}')