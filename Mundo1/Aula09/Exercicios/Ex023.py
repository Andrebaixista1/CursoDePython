from typing import Counter


numero = int(input('Digite um número: '))

unidades = numero // 1 % 10
dezenas = numero // 10 % 10
centenas = numero // 100 % 10
milhar = numero // 1000 % 10

input('''O número {} tem:
{} unidades
{} dezenas
{} centenas
{} milhares'''.format(numero, unidades, dezenas, centenas, milhar))