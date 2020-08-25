par = impar = 0
n = int(input('Digite um valor: '))
while n != 0:
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    n = int(input('Digite um valor: '))

print('FIM')
print(f'Você digitou {par} números pares e {impar} números ímpares')