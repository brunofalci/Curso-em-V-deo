# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
contgol = 0
gols = []
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# Depois vai ler a quantidade de gols feitos em cada partida. 
for c in range(0,partidas):
    g = int(input(f'Quantos gols na partida {c}?'))
    gols.append(g)
    contgol += g
jogador['gols'] = gols
jogador['total'] = contgol
print('=-'*30)
print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f' -O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c in range(len(gols)):
    print(f'  =>Na partida {c}, fez {gols[c]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do Jogador: '))
tot =int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=-' *30)
print(jogador)
print('=-' *30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')