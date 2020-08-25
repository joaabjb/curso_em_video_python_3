l1 = int(input('Digite a medida do primeiro lado: '))
l2 = int(input('Digite a medida do segundo lado: '))
l3 = int(input('Digite a medida do terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os lados FORMAM um triângulo!')
else:
    print('Os lados NÃO FORMAM um triângulo!')