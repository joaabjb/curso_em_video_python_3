from datetime import date
anoatual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = anoatual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {anoatual}.')

if idade < 18:
    print(f'Ainda vai se alistar. Falta(m) {18 - idade} anos.')
elif idade == 18:
    print('Hora de se alistar')
else:
    print(f'Já deveria ter se alistado a {idade - 18} anos.')