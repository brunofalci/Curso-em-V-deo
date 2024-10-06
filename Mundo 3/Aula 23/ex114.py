# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://tylerpalko.github.io/Is-My-Computer-ON/')
except urllib.error.URLError:
    print('O site "IsMyComputerOn" não está aceessível no momento.')
else:
    print('Consegui acessar o site "IsMyComputerOn" com sucesso!')
    print(site.read())