from random import randint
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os valores sorteados foram: ', end ='')
for n in numeros:
    print(f'{n} ', end = '')

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')   


# maior = 0
# menor = 0
# for n in numeros:
#     if n > maior:
#         maior = n
#     if n < menor:
#         menor = n
# print(f'Maior: {maior}')
# print(f'Menor: {menor}')