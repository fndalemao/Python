altura = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))
imc = peso / (altura * altura)
print(f'Seu IMC é: {imc:.2f}!')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc < 25:
    print('Você está no peso ideal!')
elif imc < 30:
    print('Você está acima do peso!')
elif imc < 40:
    print('Você está obeso!')
else:
    print('Você está em obesidade mórbida!')