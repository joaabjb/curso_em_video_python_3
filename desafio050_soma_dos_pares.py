s = 0
q = 0
for c in range(6):
    n = int(input(f'Digite {c+1}º número inteiro: '))
    if n % 2 == 0:
        q += 1
        s += n
print(f'A soma dos {q} numeros pares digitados é:', s)