vel = int(input('Digite sua velocidade: '))
if vel > 80:
    print('Você foi multado em {} reais!'.format((vel-80)*7))
else:
    print('Você está dentro do limite de velocidade!')