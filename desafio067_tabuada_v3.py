while True:
    cont = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    if n < 0:
        break
    else:
        while cont <= 10:
            print(f'{n} x {cont} = {n * cont}')
            cont += 1
    print('-'*35)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
            