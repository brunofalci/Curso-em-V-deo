import random
a1 = str(input('Nome do 1 aluno: '))
a2 = str(input('Nome do 2 aluno: '))
a3 = str(input('Nome do 3 aluno: '))
a4 = str(input('Nome do 4 aluno: '))

lista = [a1, a2, a3, a4]
print(f'O aluno sorteado apra apagar o quadro é: {random.choice(lista)}')