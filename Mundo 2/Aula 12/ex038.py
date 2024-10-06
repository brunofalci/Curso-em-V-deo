#  Escreva um programa que leia dois números inteiros e compare-os.
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2: # O primeiro valor é maior
    print('O PRIMEIRO valor é maior')
elif n2 > n1: # - O segundo valor é maior
    print('O SEGUNDO valor é maior')
else: # - Não existe valor maior, os dois são iguais
    print('Os dois valores são IGUAIS')
