# from math import hypot
# cateto_oposto = float(input('Digite o cateto oposto: '))
# cateto_adjacente = float(input('Digite o caateto adjacete: '))
# hipotenusa = hypot(cateto_oposto,cateto_adjacente)

# print(f'O comprimento da hipotenusa dos catetos {cateto_oposto} e {cateto_adjacente} é de: {hipotenusa:.2f}')

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o caateto adjacete: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print(h)
