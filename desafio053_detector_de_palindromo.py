frase = input('Digite uma frase: ').upper()
f = ''
fi = ''

#Removendo os espaços
for c in frase:
    if c != ' ':
        f += c
print(f)

#Invertendo
for c in range(len(f) - 1, -1, -1):
    fi += f[c]
print(fi)

#Comparando
if f == fi:
    print('A frase É UM PALÍNDROMO')
else:
    print('A frase NÃO É UM PALÍNDROMO')