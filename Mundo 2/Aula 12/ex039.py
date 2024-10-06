from datetime import date
# Faça um programa que leia o ano de nascimento de um jovem
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
# e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
if idade < 18 :
    saldo = 18 - idade
    alistamento = atual + saldo
    print('Ainda faltam {} para o alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(alistamento))  # tempo que falta ou que passou do prazo.
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
elif idade > 18: 
    saldo = idade - 18
    alistamento = atual - saldo
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format(alistamento)) # tempo que falta ou que passou do prazo.
