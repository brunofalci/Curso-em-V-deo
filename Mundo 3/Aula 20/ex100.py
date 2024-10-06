# # Faça um programa que tenha uma lista chamada números e duas funções
# # chamadas sorteia() e somaPar(). A primeira função vai sortear 5 numeros
# # e a vai colocá-los dentro da lista e a segunda função vai mostrar
# # a soma entre todos os valores pares sorteados pela função anterior.
# from random import randint

# def sorteia():
#     while len(numeros) < 5:
#         numeros.append(randint(0,10))
#     print('=-' * 30)
#     print(f'Os numeros sorteados foram: {numeros}')
#     print('=-' * 30)

# def somapar():
#     for valores in numeros:
#         if valores % 2 == 0:
#             pares.append(valores)
#     print(f'Os valores pares foram: {pares}')
#     print(f'=-' * 30)
#     print(f'A soma entre os valores pares é: {sum(pares)}')
#     print('=-' * 30)
# #Programa Principal
# numeros = []
# pares = []
# sorteia()
# somapar()
# print('<< PROGRAMA ENCERRADO >>')

from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
numeros = list()
sorteia(numeros)
somaPar(numeros)