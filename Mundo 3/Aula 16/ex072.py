extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis','Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze','Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:  
    num = int(input('Tente novamente. Digite um número entre 0 e 20 '))
numero_extenso = extenso[num]
print(f'Você digitou o numero:{numero_extenso}')