# notas = []
# contador = 1

# while contador <= 2:
#     notas.append(float(input(f'Escreva sua nota {contador}: ')))
#     contador += 1

# print(f'A media entre as notas é ìgual a {sum(notas)/len(notas):.2f}')
# print(notas)

# Ler duas notas de um aluno
nome = input('Digite seu nome: ')
n1 = float(input('Digite sua 1 nota: '))
n2 = float(input('Digite sua 2 nota'))

#calcular e mostrar a media
media = (n1+n2) / 2
print(f'{nome}, sua media final entre {n1:.2f} e {n2:.2f} foi de: {media:.2f}')