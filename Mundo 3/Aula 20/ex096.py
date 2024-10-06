# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

def area(larg,comp):
    a = larg * comp
    print('=-' * 30)
    print(f'A área do terreno de {larg} x {comp} é: {a:.1f} m²')
    
print('Cotrole de Terrenos'.center(30))
print('-' * 30)
l = float(input('LARGURA:(m) '))
c = float(input('COMPRIMENTO: (m) '))
area(l,c)
