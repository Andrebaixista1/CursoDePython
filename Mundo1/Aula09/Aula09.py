# Fatiamento de Strings
frase = 'Curso em Vídeo Python'
print(frase[15:]) #imprime o restante da frase
print(len(frase)) #imprime o tamanho da frase
print(frase.count('o')) #imprime a quantidade de o's
print(frase.count('o', 0, 13)) #imprime a quantidade de o's no intervalo 0 a 13
print(frase.find('deo')) #imprime a posição do primeiro 'deo'
print(frase.find('Android')) #imprime -1 se não encontrar
def cursoIn():
    if 'Curso' in frase: #imprime True se encontrar
        print(frase)
        return True
     
print(frase.replace('Python', 'Android')) #imprime a frase com a palavra substituida
print(frase.upper()) #imprime a frase em maiúsculo
print(frase.lower()) #imprime a frase em minúsculo
print(frase.capitalize()) #imprime a frase com a primeira letra em maiúsculo
print(frase.title()) #imprime a frase com as primeiras letras de cada palavra em maiúsculo
frase2 = '   Aprenda Python  '
print(frase2.strip()) #imprime a frase sem espaços em branco
print(frase2.rstrip()) #imprime a frase sem espaços em branco no final
print(frase2.lstrip()) #imprime a frase sem espaços em branco no início
print(frase.split()) #imprime uma lista com as palavras da frase
print('-'.join(frase)) #imprime a frase com '-' entre as palavras 

cursoIn()



