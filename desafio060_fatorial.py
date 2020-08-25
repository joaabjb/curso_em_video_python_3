N = int(input('Digite o número que deseja calcular o fatorial: '))
n = N
p = 1
while n > 0:
    p *= n
    n -= 1

print(f'{N}! é igual a {p}')