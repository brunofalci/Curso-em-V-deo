# Desenvolva um programa que leia seis números 
# inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

# soma = 0
# lista = []

# for c in range(1,7):
#     num = int(input('Digite um número inteiro: '))
#     lista.append(num)
#     if num % 2 == 0:
#         soma += num
# print(f'Soma dos numeros pares {soma}')
# print(f'Os números digitados foram {lista}') 

soma =0
cont = 0
for c in range(1,7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Voce informou {cont} números PARES e a soma foi {soma}')