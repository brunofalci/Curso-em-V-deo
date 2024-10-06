# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
# from datetime import date

# def voto(anonasc):
#     idade = date.today().year - anonasc
#     if idade < 16:
#         print(f'{idade} anos, VOTO NEGADO')
#     elif idade < 18 and idade > 65:
#         print(f'{idade} anos, VOTO OPCIONAL')
#     else:
#         print(f'{idade} anos, VOTO OBRIGATÓRIO')
#     print('=-' * 30)
#     print('FIM!')

# # Programa Principal

# anonasc = int(input('Em que ano você nasceu? '))
# print('=-' * 30)
# voto(anonasc)


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.' 
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
