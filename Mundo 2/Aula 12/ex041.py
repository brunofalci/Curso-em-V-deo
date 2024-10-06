# Leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print(f'O atleta tem {idade} anos')

# - Até 9 anos: MIRIM
if idade <= 9:
    print('Classificação: MIRIM')
# - Até 14 anos: INFANTIL
elif idade <= 14:
    print('Classificação: INFANTIL')
# - Até 19 anos: JÚNIOR
elif idade <= 19:
    print('Classificação: JÚNIOR')
# - Até 25 anos: SÊNIOR
elif idade <= 25 :
    print('Classificação: SÊNIOR')
# - Acima de 25 anos: MASTER
elif idade > 25 :
    print('Classificação: MASTER')