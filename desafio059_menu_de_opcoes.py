from time import sleep
p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
c = 0
sair = False

while not sair:
    c = int(input('''    [ 1 ] SOMAR 
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR DO PROGRAMA
    >>>> Qual a sua opção? '''))

    if c == 1:
        print(f'A soma entre {p} + {s} = {p + s}')
    elif c == 2:
        print(f'A multiplicação entre {p} x {s} = {p * s}')
    elif c == 3:
        if p > s:
            print(f'{p} é maior que {s}')
        elif p < s:
            print(f'{s} é maior que {p}')
        else:
            print(f'Os dois são iguais a {p}')
    elif c == 4:
        print('Digite novos números')
        p = int(input('Primeiro valor: '))
        s = int(input('Segundo valor: '))
    elif c == 5:
        sair = True
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente!!!')
    print('=-='*10)
    print()
    sleep(1.5)