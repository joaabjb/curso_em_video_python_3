print('=-='*10)
print('{: ^30}'.format('LOJA SUPER BARATÃO'))
print('=-='*10)
total = mais_de_mil = mais_barato = cont = 0
nome_mais_barato = ' '

while True:
    nome = str(input('Nome do Produto: '))
    valor = float(input('Preço: R$ '))
    total += valor
    cont += 1
    if valor > 1000:
        mais_de_mil += 1
    if cont == 1 or valor < mais_barato:
        mais_barato = valor
        nome_mais_barato = nome
    cond = ' '
    while cond not in 'SN':
        cond = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cond == 'N':
        print()
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {mais_de_mil} produto custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {nome_mais_barato} que custa R$ {mais_barato:.2f}')