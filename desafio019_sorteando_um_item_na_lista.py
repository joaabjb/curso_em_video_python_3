import random

n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

n = random.choice([n1, n2, n3, n4])

print(f'O aluno que irá apagar o quadro será {n}')