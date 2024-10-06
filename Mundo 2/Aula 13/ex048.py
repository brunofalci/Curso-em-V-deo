
# s = 0
# for c in range(1,501):
#     if  c % 2 != 0 and c % 3 == 0: 
#         s += c 
# print(s)

soma = 0
cont = 0
for c in range (1,501,2):
    if c % 3 == 0: 
        soma += c
        cont += 1
        print('-', c, end=' ')
print(f'\n\nA soma de todos os {cont} valores solicitados é {soma}')
