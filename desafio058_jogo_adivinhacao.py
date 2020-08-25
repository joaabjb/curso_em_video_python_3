from random import randint
n = randint(0,10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
c = int(input('Qual é o seu palpite? '))
cont = 1

while c != n:

    if c < n:
        print('Mais...Tente mais uma vez.')
    else:
        print('Menos...Tente mais uma vez. ')
    c = int(input('Qual é o seu palpite? '))
    cont +=1

print(f'Acertou com {cont} tentativas. Parabens!')