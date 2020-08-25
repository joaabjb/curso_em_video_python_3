s = 0
for c in range(1,500):
    if c % 2 != 0:
        if c % 3 == 0:
            s += c
print('''A soma de todos os números impares que são múltiplos 
de 3 e que estão no intervalo de 1 a 500 é''',s) 