# 1)--------------------------------------------------

# def lin():
#     print('-' * 30)

# #Programa Principal
# lin()
# print('  CURSO EM VÍDEO  ')
# lin()
# print('  APRENDA PYTHON  ')
# lin()
# print('  GUSTAVO GUANABARA')
# lin()

# 2)--------------------------------------------------

# def titulo(txt):
#     print('-' * 30)
#     print(txt)
#     print('-' * 30)

# #Programa Principal
# titulo('  CURSO EM VÍDEO  ')
# titulo('  APRENDA PYTHON  ')
# titulo('  GUSTAVO GUANABARA')
# titulo('Bruno')

# 3)--------------------------------------------------

# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a+b
#     print(f'Soma A + B = {s}')

# soma(a=4, b=5)
# soma(b=8, a=9)
# soma(7, 2)
# # soma(3,9,5) # nao funciona, parametros a mais

#  4)--------------------------------------------------

# def contador(*num):
#     for valor in num:
#         print(f'{valor} ', end='')
#     print('FIM')

# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

#  5)--------------------------------------------------

# def contador(*num):
#     tam = len(num)
#     print(f'Recebi os valores {num} que são ao todo {tam} números')
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

#  6)--------------------------------------------------
# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1

# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)

#  7)--------------------------------------------------
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
soma(5, 2)
soma (2, 9, 4)