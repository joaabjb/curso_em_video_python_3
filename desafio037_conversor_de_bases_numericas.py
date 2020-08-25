num = int(input('Digite um numero inteiro decimal: '))
print('''Escolha a base de conversão:
1: BINÁRIO
2: OCTAL
3: HEXADECIMAL''')
n = int(input('Sua opção:'))

if n == 1:
    print(f'{num} equivale a {bin(num)[2:]} em BINÁRIO.')
elif n == 2:
    print(f'{num} equivale a {oct(num)[2:]} em OCTAL.')
elif n == 3:
    print(f'{num} equivale a {hex(num).upper()[2:]} em HEXADECIMAL.')
else:
    print('Opção inválida, tente novamente!')