print('-' * 30)
print('LOJA DO HARRY')
print('-' * 30)
total = maior = menor = cont = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if cont == 1 or preco < menor:
        menor = preco
        prodMenor = produto
    if preco > 1000:
        maior += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper()
    if resp == 'N':
        break
print(f'O total da compra foi R${total:.2f}.\nTemos {maior} produto(s) custando mais de R$1000.00.\nO produto mais barato foi {prodMenor} que custa R${menor:.2f}.')