tabela = ('Internacional', 'São Paulo', 'Atlético-MG', 'Vasco',
        'Fluminense', 'Flamengo', 'Ceará', 'Palmeiras',
        'Corinthians', 'Fortaleza', 'Santos', 'Bahia',
        'Athlético-PR', 'Sport', 'Coritiba', 'Grêmio',
        'Botafogo', 'RB Bragantino', 'Atlético-GO', 'Goiás')

print('=-='*30)
print('Os cinco primeiros colocados são: ')
print(tabela[:5])
print('=-='*30)
print('Os 4 últimos são: ')
print(tabela[16:])
print('=-='*30)
print('A tabela em ordem alfabética é: ')
print(sorted(tabela))
print('=-='*30)
pos = tabela.index('São Paulo') + 1
print(f'O São paulo está na {pos}ª posição')
print('=-='*30)
#for pos, time in enumerate(tabela):
#    print(f'{pos+1}°: {time}')