from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
cont = 0

while True:
    print('=-'*15)
    n_user = int(input('Digite um valor: '))
    n_pc = randint(0,10)
    cond = ' '
    while cond not in 'PpIi':
        cond = input('Par ou impar? [P/I] ').upper().strip()[0]
    soma = n_user + n_pc
    print('-'*30)
    print(f'Você jogou {n_user} e o PC {n_pc}. Total de {soma}', end=' ')
    print('DEU PAR!' if soma % 2 == 0 else 'DEU IMPAR!')
    print('-'*30)

    if (soma % 2 == 0 and cond == 'P') or (soma % 2 != 0 and cond == 'I'):
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    else:
        print('Você Perdeu!')
        break

print('=-'*15)
print(f'GAME OVER! Você venceu {cont} vezes')