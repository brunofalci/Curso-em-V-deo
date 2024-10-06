# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120

# from math import factorial
# n = int(input('''Digite um número para calcular seu Fatorial '''))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}')

# n = int(input('''Digite um número para calcular seu Fatorial '''))
# c = n
# f = 1
# print(f'Calculando {n}! = ', end = '')
# while c > 0:
#     print(f'{c} ', end ='')
#     print(' x ' if c > 1 else ' = ', end = '')
#     f *= c
#     c -= 1
# print(f'{f}')

# n = int(input('''Digite um número para calcular seu Fatorial '''))
# fatorial = 1
# for c in range (n,0,-1):
#     print(c, end ='')
#     if c > 1:
#         print(' x ', end ='')
#     else:
#         print(' = ', end ='')
#     fatorial *= c
# print(f'{fatorial}')