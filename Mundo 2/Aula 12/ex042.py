# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo.
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Primeiro segmento: '))
r3 = float(input('Primeiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: 
    print('Os segmentos acima PODEM FORMAR triângulo ', end='')
    # - EQUILÁTERO: todos os lados iguais
    if r1 ==r2 == r3:
        print('EQUILÁTERO!')
    # - ESCALENO: todos os lados diferentes
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    # - ISÓSCELES: dois lados iguais, um diferente
    else:
        print('ISÓCELES!')  
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
