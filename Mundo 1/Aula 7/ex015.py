# quantidade de Km percorridos  e a quantidade de dias 
dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))

#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
total_diaria = dias * 60
total_km = km * 0.15 
total_geral = total_diaria + total_km

print(f'Total Diarias: {total_diaria:.2f}')
print(f'Total Km: {total_km:.2f}')
print(f'O total a pagar é de R${total_geral:.2f}')