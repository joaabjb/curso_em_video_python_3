sal = float(input('Digite o valor do salário: '))
if sal > 1250:
    print(f'O aumento será de R$ {0.1 * sal :.2f}')
else:
    print(f'O aumento será de R$ {0.15 * sal :.2f}')