# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é: {somapar}')
for l in range (0,3): # soma3col = matriz[0][2] + matriz[1][2] + matriz[2][2]
    scol+= matriz[l][2] # print(f'A soma dos valores da terceira coluna é: {soma3col}')
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c]> maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
