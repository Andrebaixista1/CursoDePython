# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request
import os
os.system('cls')

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    corAmarela = '\033[33m'
    print(f'{corAmarela}O site Pudim não está acessível no momento.\033[m')
else:
    corVerde = '\033[32m'
    print(f'{corVerde}O site Pudim está acessível no momento.\033[m')
    print(site.read())