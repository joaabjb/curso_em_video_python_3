print('Gerador de PA')
print('-=-' *6)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
n = 10

while c < n:
    print(n1, end=' -> ')
    c += 1
    n1 += r
    if c == n:
        print('PAUSA')
        n += int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {c} termos mostrados')