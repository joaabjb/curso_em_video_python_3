somaidade = 0
nomevelho = ''
idadevelho = -1
menor = 0
for c in range(1,5):
    print(f'------ {c}ª PESSOA ------')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    somaidade += idade #Acumulador da média de idade
    if sexo == 'M' and idade > idadevelho: #Homem mais velho
        idadevelho = idade
        nomevelho = nome.capitalize()
    if sexo == 'F' and idade < 20: #Mulheres menores de 20 anos
        menor += 1
media = somaidade / c
print(f'A média de idade do grupo é de {media:.1f} anos')
print(f'{nomevelho} é o homem mais velho com {idadevelho} anos')
print(f'{menor} mulher(es) tem menos de 20 anos')
        
