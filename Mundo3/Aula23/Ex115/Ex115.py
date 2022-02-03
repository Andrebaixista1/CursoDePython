import os
from lib.interface import *
from lib.arquivo import *
from time import sleep
os.system('cls')

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Criar Arquivo', 'Cadastrar Pessoas', 'Listar Pessoas', 'Sair'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Opção 3')
    elif resposta == 4:
        cabecalho('Saindo do Sistema')
        break
    else:
        cabecalho('\033[33mERRO: por favor, digite um número inteiro válido.\033[m')
    sleep(1)
    os.system('cls')

