from datetime import date
anoatual = date.today().year
maior = menor = 0
for c in range(7):
    ano = int(input(f'Em que ano a {c+1}ª pessoa nasceu: '))
    if anoatual - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade e {menor} são menores.')