print('=-='*10)
print('{:^30}'.format('BANCO JB'))
print('=-='*10)

valor = int(input('Que valor deseja sacar? R$ '))
total = valor
ced = 50
nced = 0

while True:
    if total >= ced:
        total -= ced
        nced += 1
    else:
        if nced > 0:
            print(f'Total de {nced} de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
        nced = 0
        
print('=-='*10)
print('Volte Sempre ao BANCO JB! Tenha um bom dia!')
print('=-='*10)

