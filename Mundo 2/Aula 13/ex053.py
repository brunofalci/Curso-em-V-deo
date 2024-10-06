# frase = str(input('Digite uma frase: ')).strip()
# frase_sem_espaço = frase.replace(" ","").lower()
# print(frase_sem_espaço)

# if frase_sem_espaço == frase_sem_espaço[::-1]:
#     print('palindromo')
# else:
#     print('nao palindromo')


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)-1,-1,-1):
    inverso += junto [letra]
print(junto , inverso)

if inverso == junto:
    print("Temos um palíndromo")
else:
    print('A frase digitada não é um palíndromo')
