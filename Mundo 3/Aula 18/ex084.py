# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

listatemp = []
lista = []
quantcadastro = 0
maiorpeso = []
menorpeso = []
while True:
    listatemp.append(str(input('Nome: ')))
    listatemp.append(float(input('Peso: ')))
    if len(lista) == 0 :
        maiorpeso = menorpeso = listatemp[1]
    else:
        if listatemp[1] > maiorpeso:
            maiorpeso = listatemp[1]
        elif listatemp[1] < menorpeso:
            menorpeso = listatemp[1]
    lista.append(listatemp[:])
    listatemp.clear()
    quantcadastro += 1
    c = str(input('Quer continuar ? [S/N] '))

    if c in 'Nn':
        break
print('=-' * 30)
print(f'O menor peso foi de {menorpeso}. Peso do : ', end ='')
for p in lista:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end = '')
print()
print(f'O maior peso foi de {maiorpeso}. Peso do: ', end ='')
for p in lista:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end ='')
print()
print(f'Foram cadastradas {quantcadastro} pessoas ')



# print(f'O maior peso foi de {maiorpeso}. Peso de {}')
# print(f'O menor peso foi de {menorpeso}. Peso de {}')

# temp = []
# princ = []
# mai = men = 0
# while True:
#     temp.append(str(input('Nome: ')))  
#     temp.append(float(input('Peso: ')))

#     if len(princ) == 0:
#         mai = men = temp[1]
#     else:
#         if temp[1] > mai:
#             mai = temp[1]
#         if temp[1] < men:
#             men = temp[1]

#     princ.append(temp[:])
#     temp.clear()

#     resp = str(input('Quer continuar ? [S/N] '))
#     if resp in 'Nn':
#         break
# print('-='*30)

# print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
# print(f'O maior peso foi de {mai}Kg. Peso de ', end ='')
# for p in princ:
#     if p[1] == mai:
#         print(f'[{p[0]}] ', end = '')
# print()
# print(f'O menor peso foi de {men}Kg. Peso de ', end = '')
# for p in princ:
#     if p[1] == men:
#         print(f'[{p[0]}] ', end ='')
# print()