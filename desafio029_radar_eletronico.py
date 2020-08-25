n = int(input('Digite a velocidade do carro: '))
if n > 80:
    print('Você foi multado!')
    print(f'O valor da multa é R$ {(n-80)*7:.2f}')
    