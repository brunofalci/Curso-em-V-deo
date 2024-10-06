#  Escreva um programa que leia a velocidade de um carro. 
velocidade = float(input('Qual a velocidade atual do carro? '))

# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
if velocidade > 80 : 
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de {multa:.2f}!')
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Tenha um bom dia! Dirija com segurança!')    
# A multa vai custar R$7,00 por cada Km acima do limite.