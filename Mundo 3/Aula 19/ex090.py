# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome']= str(input('Nome:'))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('-='*30)
print(f'- nome é igual a {aluno['nome']}')
print(f'- média é igual a {aluno["media"]}')
if aluno['media'] >= 7:
    print(f'    -situação é igual a Aprovado')
elif aluno['media']<= 5:
    print('-situação é Reprovado')
else:
    print('-situação é igual a Recuperação')