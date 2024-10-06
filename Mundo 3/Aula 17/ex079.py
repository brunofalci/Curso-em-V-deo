# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

listavalores = []
num = []
while True:
    num = int(input('Digite um valor: '))
    if num in listavalores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        listavalores.append(num)
        print('Valor adicionado com sucesso...')
    continuar = str(input('Quer continuar? [S/N]:')).upper().strip()
    if continuar in 'Nn':
        break 
print('=-'*30)


listavalores.sort()
print(f'Você digitou os valores {listavalores}')

