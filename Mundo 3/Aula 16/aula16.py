# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita' )
# # Tuplas são imutaveis
# # lanche[1] = 'Refrigerante' # nao funciona, tuplas sao imutaveis


# #acessar a tupla sem pegar posição
# for comida in lanche:
#     print(f'Eu vou comer {comida}')

# # maneira 1 de acessar a tupla pegando a posição
# for cont in range(0,len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# # maneira 2 de acessar a tupla
# for pos,comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')

# print('Comi pra caramba!')

# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita' )

# print(sorted(lanche)) #só imprime o valor ordenado, nao organiza pra voce
# print(lanche)

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = b + a # nao soma valores, somente junta eles (2, 5, 4, 5, 8, 1, 2)
# print(c)
# print(c.index())

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)
print(pessoa)

