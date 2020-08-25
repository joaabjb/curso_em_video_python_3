print('Digite três números inteiros diferentes')
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print(f'{n1} é o maior e {n3} é o menor')
        else:
            print(f'{n1} é o maior e {n2} é o menor')
    else:
        print(f'{n3} é o maior e {n2} é o menor')

else:
    if n2 > n3:
        if n1 > n3:
            print(f'{n2} é o maior e {n3} é o menor')
        else:
            print(f'{n2} é o maior e {n1} é o menor')
    else:
        print(f'{n3} é o maior e {n1} é o menor')
