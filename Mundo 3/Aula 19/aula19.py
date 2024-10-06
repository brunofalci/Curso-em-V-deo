# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# pessoas['nome'] = 'Leandro'
# pessoas['peso'] = 98.5
# # del pessoas['sexo']
# # print(pessoas[0]) da erro por que é dic e ñ lista
# print(pessoas['nome'])
# print(pessoas['idade'])
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# print('-'*30)
# for k in pessoas.keys():
#     print(k)
# for k in pessoas.values():
#     print(k)
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# ------------------------------------------------------------------
brasil = []
estado0 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado0)
brasil.append(estado1)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado = {}
brasil = []
for c in range (0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # brasil.append(estado) não funciona pq tem que fazer copia da lista estado[:]
    brasil.append(estado.copy()) # Jeito correto de fazer a cópia da lista
'''print(brasil)
print('=-'*30)'''
'''for e in brasil:
    for k, v in e.items():
        print(f'O campo {k}, tem valor: {v}. ', end =' ')
    print()'''
for e in brasil:
    for v in e.values():
        print(v, end =' ')
    print()