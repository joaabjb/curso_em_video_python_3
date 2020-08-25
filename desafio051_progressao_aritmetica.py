n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

for c in range(n1, n1 + 10*r, r):
    print(c, end=' -> ')
print('FIM')



'''
s = n1
for c in range(10):
    s = n1 + c*r
    print(s, end=' -> ')
print('FIM')
'''

