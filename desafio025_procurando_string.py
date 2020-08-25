nome = input('Digite o seu nome: ')
cond = 'SILVA' in nome.upper()
print(f'O seu nome tem "Silva"? (True/False): {cond}')


#Outra forma
nome = input('Digite o seu nome: ')
print('Tem Silva no nome?', 'silva' in nome.lower())