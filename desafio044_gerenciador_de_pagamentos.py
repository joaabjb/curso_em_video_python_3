val = float(input('Digite o valor do produto: '))
print('''Escolha a opção de pagamento:
[ 1 ] A vista dinheiro / cheque
[ 2 ] A vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
cond = int(input('Digite a opção: '))

if cond == 1:
    print(f'O valor a ser pago será R$ {0.9 * val :.2f}')
elif cond == 2:
    print(f'O valor a ser pago será R$ {0.95 * val :.2f}')
elif cond == 3:
    print(f'O valor a ser pago será RS {val :.2f}')
elif cond == 4:
    print(f'O valor a ser pago será R$ {1.2 * val :.2f}')
else:
    print('opção inválida, tente novamente')