from random import randint
from time import sleep
print('''Escolha a opção:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
j = int(input('Sua opção: '))
n = randint(1,3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

if j == 1:
    print ('Você jogou PEDRA')
    if n == 1:
        print('Computador jogou PEDRA')
        print('EMPATE!')
    elif n == 2:
        print('Computador jogou PAPEL')
        print('VOCÊ PERDEU!')
    elif n == 3:
        print('Computador jogou TESOURA')
        print('VOCÊ VENCEU!')
elif j == 2:
    print ('Você jogou PAPEL')
    if n == 1:
        print('Computador jogou PEDRA')
        print('VOCÊ VENCEU!')
    elif n == 2:
        print('Computador jogou PAPEL')
        print('EMPATE!')
    elif n == 3:
        print('Computador jogou TESOURA')
        print('VOCÊ PERDEU!')
elif j == 3:
    print ('Você jogou TESOURA')
    if n == 1:
        print('Computador jogou PEDRA')
        print('VOCÊ PERDEU!')
    elif n == 2:
        print('Computador jogou PAPEL')
        print('VOCÊ VENCEU!')
    elif n == 3:
        print('Computador jogou TESOURA')
        print('EMPATE!')
else:
    print('Opção inválida')