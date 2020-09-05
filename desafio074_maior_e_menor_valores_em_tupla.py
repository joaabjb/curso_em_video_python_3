from random import randint
lista = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
maior = menor = -1
print('Os valores sorteados são: ', end='')
for n, numero in enumerate(lista):
    print(numero, end=' ')
    if n == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
print()
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')