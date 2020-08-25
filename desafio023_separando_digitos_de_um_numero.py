num = int(input('Digite um numero entre 0 e 9999: '))


u = num % 10
d = (num // 10) % 10
c = (num // 100) % 10
um = num // 1000

print(f'''Análise do número {num}
    unidade: {u}
    dezena : {d}
    centena: {c}
    milhar: {um}''')
