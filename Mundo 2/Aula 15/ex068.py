# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint
print('=-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*30)
while True:
    computador = randint(1,10)
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar ? [P/I] ')).upper()[0].strip()
    soma = computador + jogador
    vezesvenc = 0
    if escolha in 'P':
        if soma % 2 == 0:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR.')
            vezesvenc += 1
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR.')
            break
    elif escolha in 'I':
        if soma % 2 != 0:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR.')
            break
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR.')
            vezesvenc += 1
    print('Vamos jogar novamente!')
print('VOCÊ PERDEU!')
print('=-'*30)
print(f'GAME OVER! Você venceu {vezesvenc} vezes.')       

