preco = float(input('Digite o valor do produto: R$'))
print('Escolha a forma de pagamento:\n[1] À vista (Dinheiro/Cheque)\n[2] À vista no cartão\n'
      '[3] Em 2x no cartão\n[4] 3x ou mais no cartão')
pgmt = int(input('Opção: '))
if pgmt == 1:
    preco = preco - preco * 0.1
elif pgmt == 2:
    preco = preco - preco * 0.05
elif pgmt == 3:
    print(f'O valor de cada parcela será de R${preco / 2:.2f}')
elif pgmt == 4:
    preco = preco + preco * 0.2
    par = int(input('Quanta parcelas? '))
    print(f'O valor de cada parcela será de R${preco / par:.2f}')
else:
    print('OPÇÃO INVÁLIDA!')
print(f'O valor final do seu produto será de R${preco:.2f}')