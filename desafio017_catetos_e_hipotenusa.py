from math import sqrt, pow

c1 = int(input('Digite a medida do primeiro cateto: '))
c2 = int(input('Digite a medida do segundo cateto: '))

h = sqrt(pow(c1,2) + pow(c2,2))

print(f'A medida da hipotenusa será {h:.2f}')