dist = float(input('Digite a distância de sua viagem: '))
valor = 0
if dist <= 200:
    valor = dist * 0.5
else:
    valor = dist * 0.45
print('O valor da sua passagem é R${:.2f}'.format(valor))