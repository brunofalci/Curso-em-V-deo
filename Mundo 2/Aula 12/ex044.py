# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
print('=========== LOJAS GUANABARA ===========')
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual sua opção? '))
# - à vista dinheiro/cheque: 10% de desconto
if opcao == 1:
    total = preco - (10/100 * preco)
# - à vista no cartão: 5% de desconto
elif opcao == 2:
    total = preco - (5/100 * preco)
# - em até 2x no cartão: preço formal
elif opcao == 3:
    total = preco
    print(f'Sua compra será parcelada em 2x de {(total/2):.2f} SEM JUROS')
# - 3x ou mais no cartão: 20% de juros
elif opcao == 4:
    total = preco + (20/100 * preco) 
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de {parcela:.2f} COM JUROS')
else:
    total = preco
    print('OPÇÃO INVALIDA de pagamento. Tente novamente!')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')

