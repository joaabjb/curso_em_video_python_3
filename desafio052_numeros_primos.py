num = int(input('Digite um número inteiro: '))
cont = 0

for c in range(1, num+1):
    if num % c == 0:
        cont += 1
        print(f'\033[34m{c}', end=' ')
    else:
        print(f'\033[31m{c}', end=' ')
print('\033[m')
if cont == 2:
    print('O número É PRIMO!')
else:
    print('O número NÃO É PRIMO!')
