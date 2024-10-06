# num = int(input('Digite um numero inteiro: '))
# divisores = 0
# for i in range(1,num+1):
#     if num % i == 0:
#         divisores += 1
# if divisores == 2:
#     print(f'{num} é um número primo')
# else:
#     print(f'{num} não é um número primo')

num = int(input('Digite um numero: '))
tot = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO numero {num} foi divisível {tot} vezes')
if tot == 2:
    print(' E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
