larg = float(input('Digite em metros a largura da parede: '))
alt = float(input('Digite em metros a altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede possui uma área de {:.2f}m² e você presisará de {:.2f}L de tinta para pintá-la'.format(area, tinta))