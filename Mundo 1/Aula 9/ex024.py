# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cid = str(input('Em qual cidade voce nasceu ? ')).strip()
cidade = cid.lower()
print(cidade[:5] == 'santo')