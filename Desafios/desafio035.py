#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um tirângulo
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s1 < s2 + s3 and s3 < s2 + s1:
    print('OS SEGMENTOS DIGITADOS PODEM FORMAR UM TRIÂNGULO')
else:
    print('OS SEGMENTOS DIGITADOS NÃO PODEM FORMAR UM TRIÂNGULO')