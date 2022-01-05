import math
# catOposto = float(input('Comprimento do cateto oposto: '))
# catAdjacente = float(input('Comprimento do cateto adjacente: '))
# hi = (catOposto ** 2 + catAdjacente ** 2) ** (1/2)
# print('A hipotenusa é {:.2f}'.format(hi))

catOposto = float(input('Comprimento do cateto oposto: '))

catAdjacente = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(catOposto, catAdjacente)
print('A hipotenusa é {:.2f}'.format(hi))