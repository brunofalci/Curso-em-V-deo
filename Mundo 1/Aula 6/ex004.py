algo = input("Digite algo: ")
print('O tipo primitivo desse valor é ', type(algo))
print('Só tem espaço ?', algo.isspace())
print('É um numero?', algo.isnumeric())
print('É alfabetico?', algo.isalpha())
print('É alfanumerico? ', algo.isalnum())
print('Esta em maiusculas?', algo.isupper())
print('Esta em minusculo', algo.islower())
print('Esta Captalizizado', algo.istitle())