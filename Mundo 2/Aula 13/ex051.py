''' Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão.'''

# prim = int(input("Primeiro termo: \n"))
# raz = int(input("Digite a razão da PA: \n"))
# dec = prim + (10 - 1) * raz  # Fórmula do enésimo termo de uma PA.
# for c in range(prim, dec+raz, raz):
#     print("{}".format(c), end="->")
# print("Fim.")

print('='*12)
print('   10 TERMOS DE UMA PA   ')
print('='*12)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10-1) * razão
for c in range (primeiro, decimo+razão, razão):
    print(f'{c}', end='-> ')
print('Acabou')

