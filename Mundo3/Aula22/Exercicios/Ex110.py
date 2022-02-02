

import moeda as md
import os
os.system('cls')


p = float(input('Digite o preço: R$ '))
print(f'A metade de {md.moeda(p)} é {md.metade(p, True)}')
print(f'O dobro de {md.moeda(p)} é {md.dobro(p, True)}')
print(f'Aumentando 10%, temos {md.aumentar(p, 10, True)}')
print(f'Diminuindo 13%, temos {md.diminuir(p, 13)}')