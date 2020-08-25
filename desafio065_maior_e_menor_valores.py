cont = soma = 0 
maior = menor = 0
cond = 'S'

while cond == 'S':
    n = int(input('Digite um número: '))
    soma += n
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    cont += 1
    cond = input('Quer continuar? [S/N] ').upper().strip()[0]

media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')