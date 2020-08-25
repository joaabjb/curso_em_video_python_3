frase = input('Digite uma frase: ').lower().strip()

print('A letra "a" aparece {} vezes'.format(frase.count('a')) )
print('A primeira letra "a" aparece na posição {}'.format(frase.find('a')+1))
print('A ultima letra "a" aparece na posição {}'.format(frase.rfind('a')+1))


#Outra forma
frase = input('Digite uma frase: ')
print('A letra "a" aparece', frase.lower().count('a'), 'vezes')
print('Ela aparece a primeira vez na posição', frase.lower().find('a'))
print('Ela aparece pela ultima vez na posiçao', frase.lower().rfind('a'))