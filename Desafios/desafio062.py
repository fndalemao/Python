num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
termo = num
total = 0
mais = 10
while mais > 0:
    total = total + mais
    while cont < total:
        print(termo, end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer momstrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')