# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}')
# - Média 7.0 ou superior: APROVADO
if media >= 7:
    print('O aluno esta APROVADO')
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
elif media >= 5 and media <= 6.9: 
    print('O aluno esta RECUPERAÇÃO')
# - Média abaixo de 5.0: REPROVADO
elif media < 5 :
    print('O aluno esta REPROVADO')
