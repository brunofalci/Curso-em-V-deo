from random import randint
from time import sleep
computador = randint(1,5) # numero pc

print('-=-'*27)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*27)

jogador = int(input('Em que número eu pensei? ')) #numero jogador
print('PROCESSANDO...')
sleep(2)
if jogador == computador :
    print(f'PARABÉNS" Você conseguiu me vencer!')
else: 
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}')