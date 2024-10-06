# Crie um programa onde o usuário possa digitar sete valores numéricos 
# e cadastre-os em uma lista única que mantenha separados os valores
# pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.
num = [[], []]
valor = 0 
for c in range(1,8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=-'*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')

# lista = []
# listatemp = []
# listaimpar = []
# listapar = []
# for i in range (0,7):
#     n = int(input(f'Digite o {i+1} número: '))
#     if n % 2 == 0:
#         listapar.append(n)
#     elif n % 2 != 0 :
#         listaimpar.append(n)
# listapar.sort()
# listaimpar.sort()
# lista.append(listapar)
# lista.append(listaimpar)
# print('=-'*30)
# print(f'Os valores pares digitados foram: {lista[0]}')
# print(f'Os valores ímpares digitados foram: {lista[1]}')
# print(f'A lista completa em ordem é: {lista}')
