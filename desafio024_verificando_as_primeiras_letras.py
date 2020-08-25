nome = input('Digite o nome da cidade: ').split()
cond = 'SANTO' in nome[0].upper()
print(f'O nome da cidade começa com Santo? (True/False): {cond}')


#OUTRA FORMA DE FAZER
cidade = input('Digite o nome da cidade: ')
print('A cidade começa com Santo?', 'santo' in cidade.lower().split()[0])