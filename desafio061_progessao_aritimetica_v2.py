print('Gerador de PA')
print('-=-' *6)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0

while c < 10:
    print(n1, end=' -> ')
    c += 1
    n1 += r
print('FIM')