# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não 
# tenha sido informado corretamente.
def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} marcou {gol} gol(s) no campeonato ')

nome = str(input('Nome do Jogador: '))
g = str(input('Quantos gols marcou ? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    ficha(gol = g)
else:
    ficha(nome, g)

# def ficha(jog='<desconhecido>', gol=0):
#     print(f'O jogador {jog} fez {gol} gol(s) no campeonato. ')

# #Programa Principal
# n = str(input('Nome do Jogador: '))
# g = str(input('Número de Gols: '))
# if g.isnumeric():
#     g=int(g)
# else:
#     g = 0
# if n.strip() == '':
#     ficha(gol = g)
# else:
#     ficha(n, g)