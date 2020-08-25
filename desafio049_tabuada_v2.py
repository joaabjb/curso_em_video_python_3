n = int(input('Digite um número inteiro: '))
print(f'Tabuada do Número {n}')
for c in range(11):
    print(f'{n} + {c:2} = {n + c:2}     {n} x {c:2} = {n*c:2}')