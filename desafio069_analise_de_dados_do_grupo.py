maior = homem = mulher_menor = 0

while True:
    print('=-'*15)
    print('CADASTRE UMA PESSOA')
    print('=-'*15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulher_menor += 1    
    cond = ' '
    while cond not in 'SN':
        cond = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cond == 'N':
        break

print('-'*30)
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher_menor} mulher(es) com menos de 20 anos')