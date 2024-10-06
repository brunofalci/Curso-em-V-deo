# pergunte o salário de um funcionário e calcule o valor do seu aumento. 
salario = float(input('Qual é o salário do funcionário? R$'))
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
if salario > 1250.00:
    novo = salario + (salario * 10 / 100)
# Para os inferiores ou iguais, o aumento é de 15%.
else:
    novo = salario * 1.15
print(f'Quem ganhava {salario:.2f} passa a ganhar R${novo:.2f} agora')