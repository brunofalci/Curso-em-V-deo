# Crie um programa que leia o ano de nascimento de sete pessoas.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1,8):
    nascimento = int(input(f'Em que ano a {pess} pessoa nasceu ? '))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemor {totmaior} pessoas maiores de idade')
print(f'Ao todo tivemor {totmenor} pessoas menores de idade')

# No final, mostre quantas pessoas ainda não atingiram a maioridade 
# e quantas já são maiores.