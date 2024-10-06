# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura (m) '))
# calcule seu Índice de Massa Corporal (IMC) 
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
# mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
# - Entre 18,5 e 25: Peso Ideal
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
# - 25 até 30: Sobrepeso
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
# - 30 até 40: Obesidade
elif 30 <= imc < 40:
    print('Você esta em OBESIDADE')
# - Acima de 40: Obesidade Mórbida
elif imc > 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
