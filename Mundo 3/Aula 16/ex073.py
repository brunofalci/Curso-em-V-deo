listadetimes = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('--'*70)
print(f'Lista de times do Brasileirão: {listadetimes}')
print('--'*70)
print(f'Os 5 primeiros são {listadetimes[:6]}') # 5 primeiros colocados
print('--'*70)
print(f'Os 4 últimos são {listadetimes[-4:]}')# 4 ultimos colocados
print('--'*70)
print(f'Times em ordem alfabética: {sorted(listadetimes)}') # lista organizada em ordem alfabetica
print('--'*70)
for pos, time in enumerate(listadetimes):
    if time == 'Chapecoense':
        print(f'O Chapecoense esta na {pos+1} posição')
      