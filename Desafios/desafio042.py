s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s1 < s2 + s3 and s3 < s2 + s1:
    print('OS SEGMENTOS DIGITADOS PODEM FORMAR UM TRIÂNGULO.')
    if s1 == s2 == s3:
        print('TRIÂNGULO EQUILÁTERO!')
    elif s1 == s2 and s1 != s3 or s2 == s3 and s2 != s1 or s1 == s3 and s1 != s2:
        print('TRIÂNGULO ISÓCELES!')
    else:
        print('TRIÂNGULO ESCALENO!')
else:
    print('OS SEGMENTOS DIGITADOS NÃO PODEM FORMAR UM TRIÂNGULO')