# Escreva um programa que leia um número N inteiro qualquer e 
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

# print('-'*30)
# print('Sequência Fibonacci')
# print('-'*30)
# n = int(input('Quantos termos você quer mostrar ? '))
# t1 = 0
# t2 = 1
# print('~'*30)
# print(f'{t1} -> {t2}', end = '')
# cont = 3
# while cont <= n:
#     t3 = t1 + t2
#     print(f' -> {t3}', end = '')
#     t1 = t2
#     t2 = t3
#     cont += 1
# print(' -> FIM')
# print('~'*30)


n = int(input('Quantos termos vc quer mostrar? '))
n1 = 0
n2 = 1
n3 = n1+n2
cont = 3
print(f'{n1}, {n2}, ',end ='')
while cont <= n:
    n3 = n1 + n2
    print(f'{n3},', end = ' ')
    n1 = n2
    n2 = n3
    cont += 1
print('Fim')

