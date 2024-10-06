# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# def fatorial(num, show=False):
#     """
#     -> Calcula o Fatorial de um número.
#     :param num: O número a ser calculado
#     :param show: (opcional) Mostrar ou não a conta.
#     :return: O valor fatorial de um número n.
#     """
#     fat = 1
#     for c in range (num, 0, -1):
#         fat *= c
#         if show == True:
#             print(f'{c} x ', end='')
#     print(f'= {fat}')
#     return fat


# # num = int(input('Qual numero deseja saber o fatorial ? '))
# fatorial(5, show=True)
# # help(fatorial)

def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end ='')
            if c>1:
                print(f' x ', end ='')
            else:
                print(' = ', end ='')
        f *= c
    return f

# Programa Principal
print(fatorial(5, show=False))
help(fatorial)

