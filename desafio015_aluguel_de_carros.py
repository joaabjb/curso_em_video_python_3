#Calculo de aluguel

dist = float(input('Digite a quantidade de km rodados: '))
dias = int(input('Digite a quantidade de dias com o carro: '))

v = dist * 0.15 + dias * 60

print(f'O valor a ser pago será R$ {v:.2f}')