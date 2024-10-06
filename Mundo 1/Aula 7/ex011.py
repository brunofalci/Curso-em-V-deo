#Ler a altura e largura de uma parede em metros.
altura = float(input('Informe a altura da parede em metros: '))
largura = float(input('Informe a largura da parede em metros: '))

#Calcular a área 
area = altura * largura
print(f'A area da parede é de {area:.2f}m²')

#Calcular quantidade de tinta (1L = 2m²)
print(f'A quantidade de tinta é {(area/2):.2f} litros')