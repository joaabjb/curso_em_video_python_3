n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print(f'A média das notas é {media} e o aluno está ', end='')
if media < 5:
    print('REPROVADO')
elif media >= 7:
    print('APROVADO')
else:
    print('EM RECUPERAÇÃO')