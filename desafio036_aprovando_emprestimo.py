valor = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do salário: '))
anos = int(input('Digite em quantos ano irá pagar: '))
prest = valor / (anos * 12)

if prest > (0.3*sal):
    print(f'Empréstimo negado, prestação excedeu 30% do salário!')
else:
    print('Empréstimo aprovado!')