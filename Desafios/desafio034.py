sal = float(input('Digite o salário: R$'))
if sal <= 1250.00:
    sal = sal + (sal * 0.15)
else:
    sal = sal + (sal * 0.10)
print(f'O salário ajustado é R${sal:.2f}')