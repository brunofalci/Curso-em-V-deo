# # Interactive Help
# print('Olá Mundo')
# help(print)
# help(input)
# print(input.__doc__)
# help(input)

# ********************************************************************

# # Docstrings
# def contador(i,f,p):
#     """ 
#     -> Faz uma contagem e mostra na tela
#     :param i: inicio da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     Função criada por Gustavo Guanabara do canal CursoemVídeo
#     """
#     c=i
#     while c <= f:
#         print(f'{c} ',end='..')
#         c += p
#     print('FIM!')

# # contador(2,10,2)
# help(contador)

# ********************************************************************************

# Parâmmetros Opcionais

# def somar(a=0,b=0,c=0):
#     """ 
#     -> Faz uma soma de três valores  e mostra na tela
#     :param a: 1 valor
#     :param b: 2 valor
#     :param c: 3 valor
#     Função criada por Gustavo Guanabara do canal CursoemVídeo
#     """
#     s=a+b+c
#     print(f'A soma vale {s}')

# somar(3,2,5)
# somar(8,4)
# somar (b=4, c=2)
# somar(c=3, a=2)
# somar()

# ********************************************************************************

# # Escopo de Variáveis

# def teste():
#     x=8 #variável local
#     print(f'Na função teste, n vale {n}')
#     print(f'Na função teste, x vale {x}')
# #Programa principal
# n=2 #variável global
# print(f'No programa principal, n vale {n}')
# # print(f'No programa principal, x vale {x}') #vai dar erro x só existe dentro da função teste(), x é variavel local e nao global
# teste()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# def funcao():
#     n1=4 #local
#     print(f'N1 dentro vale {n1}')

# n1 = 2 #global
# funcao()
# print(f'N1 fora vale {n1}')

# -------------------------------------------------

# def teste(b):
#     global a 
#     a=8
#     b+= 4
#     c=2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')

# a=5
# teste(a)
# print(f'A fora vale {a}')

# ********************************************************************************

# # Retornando Valores
# def somar(a=0,b=0,c=0):
#     s=a+b+c
#     # print(f'A soma vale {s}')
#     return s

# r1 = somar(3, 2, 5)
# r2 = somar (1, 7)
# r3 = somar(4)
# print(f'Meus cálculos deram {r1}, {r2} e {r3}.' )

# ********************************************************************************

# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f

# # n = int(input('Digite um numero: '))
# # print(f'O fatorial de {n} é igual a {fatorial(n)}')

# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2} e {f3}')

# -------------------------------------------------------------------------

def par(n=0):
    if n%2 ==0:
        return True
    else:
        return False
    

num = int(input('Digite um número:'))
print(par(num))
if par(num):
    print('É par')
else:
    print('É ímpar')