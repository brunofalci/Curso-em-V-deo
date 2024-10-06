# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
distancia = int(input('Qual é a distância da sua viagem? '))
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
if distancia <= 200:
    preco = distancia * 0.5
    print(f'Você está prestes a começar uma viagem de {distancia:.1f}Km')
    print(f'E o preço da sua passagem será de R${preco:.2f}')
# R$0,45 parta viagens mais longas.
else:
    preco = distancia * 0.45
    print(f'Você está prestes a começar uma viagem de {distancia:.1f}Km')
    print(f'E o preço da sua passagem será de R${preco:.2f}')