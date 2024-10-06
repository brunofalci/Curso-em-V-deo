#  Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

# print('='*12)
# print('   10 TERMOS DE UMA PA   ')
# print('='*12)

# primeiro = int(input('Primeiro termo: '))
# razão = int(input('Razão: '))
# decimo = primeiro + (10-1) * razão
# for c in range (primeiro, decimo+1, razão):
#     print(f'{c}', end='-> ')
# print('Acabou')

print('Gerador de PA')
print('='*10)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1 
while cont <= 10:
    print(f'{termo} -> ', end = '')
    termo += razão
    cont += 1
print ('Fim')

# primeiro_termo = int(input("Digite o primeiro termo da PA: "))
# razao = int(input("Digite a razão da PA: "))
# termo_atual = primeiro_termo
# contador = 1

# print("Os 10 primeiros termos da PA são:")

# while contador <= 10:
#     print(termo_atual, end=" ")
#     termo_atual += razao
#     contador += 1

# print()