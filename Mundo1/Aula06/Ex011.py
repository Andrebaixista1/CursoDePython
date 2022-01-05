largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura

print('Sua parede tem a dimensão de {}x{} e sua area tem {}m²'.format(largura,altura,area))

tinta = area/15
print('Você precisa de {} lt de tinta'.format(tinta))