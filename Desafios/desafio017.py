from math import hypot
catO = float(input('Digite o comprimento em centímetros do cateto oposto: '))
catA = float(input('Digite o comprimento em centímetros do cateto adjacente: '))
hip = hypot(catO, catA)
print('Sua hipotenusa tem {:.2f}cm de comprimento'.format(hip))