import random
import math
import emoji

# print(emoji.emojize('Olá mundo :globe_showing_Americas:'))  //https://pypi.org/search/?q=emoji
# Olá mundo 🌎

# math.ceil()  //arredonda um numero p cima
# math.floor() //arredonda um numero p baixo
# math.trunc() //trunca um numero (apresenta somente o num antes da , > 6,223=6)
# math.pow() //calcula potenci
# math.sqrt //calcula raiz quadrada
# math.factorial() //calcula fatorial de um num = 3!= 3*2*1 ==6

num = int(input('Digite um numero'))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')

num = random.randint(1,10)
print(num)

print(emoji.emojize("Ola mundo :globe_showing_Americas:"))