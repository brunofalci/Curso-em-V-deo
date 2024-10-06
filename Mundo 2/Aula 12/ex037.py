num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input(('Sua opção: ')))

if opcao == 1:
    binario = bin(num)
    print(f'{num} em BINÁRIO é igual a {binario[2:]}')
elif opcao == 2:
    octal = oct(num)
    print(f'{num} em OCTAL é igual a {octal[2:]}')
elif opcao == 3: 
    hexadecimal = hex(num)
    print(f'{num} em OCTAL é igual a {hexadecimal[2:]}')

else: 
    print('Opção inválida, tente novamente')