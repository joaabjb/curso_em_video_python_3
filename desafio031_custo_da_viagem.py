d = int(input('Dgite a distância da viagem em Km: '))
if d <= 200:
    print(f'O preço da passagem será R$ {0.50 * d :.2f}')
else:
    print(f'O preço da passagem será R$ {0.45 * d :.2f}')

