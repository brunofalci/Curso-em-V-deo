# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
minimo = salario * 30 / 100

print(f'Pra pegar uma casa de R${casa:.2f} em {anos} anos', end='')
print (f' a prestação será de R${prestacao:.2f}')

if prestacao <= minimo:
    print('Empréstimo CONCEDIDO!')
else:    
    print('Empréstimo NEGADO!')


# print('Empréstimo NEGADO!')
# print('Empréstimo CONCEDIDO!')