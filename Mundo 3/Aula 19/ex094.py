# #  Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# # A) Quantas pessoas foram cadastradas
# # B) A média de idade
# # C) Uma lista com as mulheres
# # D) Uma lista de pessoas com idade acima da média
# listapessoas = []
# while True:
#     pessoas = {}
#     pessoas['nome'] = str(input('Nome: '))
#     pessoas['idade'] = int(input('Idade: '))
#     pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()
#     listapessoas.append(pessoas)
#     continuar = str(input('Deseja continuar ?[S/N]: '))
#     if continuar in 'Nn':
#         break
# print()
# print('=-'*30)
# # A) Quantas pessoas foram cadastradas
# print(f'Foram cadastradas {len(listapessoas)} pessoas')
# # B) A média de idade
# soma_idade = 0
# for pessoa in listapessoas:
#     soma_idade += pessoa['idade']
# media_idade = soma_idade / len(listapessoas)
# print(f'A média de idade foi {media_idade}')
# # C) Uma lista com as mulheres
# lista_mulheres = []
# for pessoa in listapessoas:
#     if pessoa['sexo'] == 'F':
#         lista_mulheres.append(pessoa['nome'])
# print(f'A lista com nome das mulheres é: {lista_mulheres}')
# # D) Uma lista de pessoas com idade acima da média
# lista_idade = []
# for pessoa in listapessoas:
#     if pessoa['idade'] > media_idade:
#         lista_idade.append(pessoa['nome'])
# print(f'A lista com pessoas acima da média de idade é: {lista_idade}') 

galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF': 
            break
        print('ERRO! Por favor, digite apenas M ou F. ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas [S/N]')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}, ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
