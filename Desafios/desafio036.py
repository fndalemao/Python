#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
#do comprador e em quantos anos ele vai pagar. A prestação, não pode exceder 30% do salário ou então o emprestimo será negado
casa = float(input('Qual é o valor do imóvel? R$'))
salario = float(input('Qual é o valor do seu salário? R$'))
anos = int(input('Quantas prestações deseja pagar (anos)?'))
meses = anos * 12
prestacao = casa / meses
print(f'Para pagar um imóvel de R${casa:.2f} em {anos} anos a mensalidade será de R${prestacao:.2f}')
if prestacao <= (salario * 0.3):
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')