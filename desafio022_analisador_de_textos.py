nome = str(input('Digite o seu nome completo: '))

print(nome.upper())
print(nome.lower())
num_letras = len(nome) - nome.count(' ')
print(f'{num_letras} letras no total')
n = nome.split()
print(f'O primeiro nome tem {len(n[0])} letras')


nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
print('Letras ao todo:', len(nome) - nome.count(' '))
print('Quantidade de letras do primeiro nome:', len(nome.split()[0]))