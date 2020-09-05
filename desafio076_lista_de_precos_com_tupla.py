lista = ('Lápis', 1.75,
        'Borracha', 2,
        'Caderno', 15.90,
        'Estojo', 25,
        'Transferidor', 4.20,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.30,
        'Livro', 34.90)
print('=-='*13)
print(f'{"LISTA DE PREÇOS":^39}')
print('=-='*13)
for c in range(len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'R$ {lista[c]:>6.2f}')
print('=-='*13)