peso = float(input('Digite o peso: '))
alt = float(input('Digite a altura: '))

imc = peso / alt**2
print(f'O IMC da pessoa é de {imc:.1f} e ela está ', end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('NO PESO IDEAL')
elif imc < 30:
    print('COM SOBREPESO')
elif imc < 40:
    print('COM OBESIDADE')
else:
    print('COM OBESIDADE MÓRBIDA')