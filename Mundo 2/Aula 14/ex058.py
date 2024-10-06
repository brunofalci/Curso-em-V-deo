# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

# from random import randint
# computador = randint(1,11) # numero pc
# print('''Sou seu computador ...
# Acabei de pensar em um número entre 0 e 10.
# Será que você consegue adivinhar qual foi ?''')
# jogador = 0
# cont = 0
# while jogador != computador: 
    
#     jogador = int(input('Qual o seu palpite ')) #numero jogador
    
#     if jogador == computador :
#         cont += 1
#         print(f'Acertou com {cont} tentativas. Parabéns!')    
#     else:
#         if jogador < computador : 
#             print(f'Mais, tente mais uma vez')
#         elif jogador > computador: 
#             print(f'Menos, tente mais uma vez')
#     cont += 1

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de penser em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi ?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador: 
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
            
print(f'Acertou com {palpites} tentativas. Parabéns!')
