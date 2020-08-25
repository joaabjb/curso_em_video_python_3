print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
print('~'*30)
c = 0
ant = 0
atual = 1

while c < n:
    if c == 0 :
        print(ant, end = ' -> ')
    elif c == 1:
        print(atual, end = ' -> ')
    else:
        prox = ant + atual
        ant = atual
        atual = prox
        print(atual, end = ' -> ')
    c += 1

print('FIM')
print('~'*30)