from Mundo3.Aula22.Exercicios.arquivos import dado

dado()

def moeda(preco=0, moeda='R$ ', typemd=False):
    return f'{moeda}{preco:>.2f}'.replace('.',',')