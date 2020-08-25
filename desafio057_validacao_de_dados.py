sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
while sexo not in 'MFmf':
    sexo = input('Valor inválido. Digite novamente: ').strip().upper()[0]
print(f'Sexo {sexo} Registrado com sucesso!')