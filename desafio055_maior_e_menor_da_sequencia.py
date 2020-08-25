maior = menor = 0
for c in range(5):
    peso = float(input(f'Peso da {c+1}ª pessoa: '))
    if c == 0: #Primeiro laço
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior} kg, e o menor é {menor} kg')
