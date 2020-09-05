lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

#for comida in lanche:
#    print(comida)

#for c in range(len(lanche)):
#    print(f'{c+1}° vou comer {lanche[c]}')

#for c, comida in enumerate(lanche):
#    print(f'{c+1}° vou comer {comida}')

#print(f'Comi pra caramba!')

#print(sorted(lanche)) #Mostra em ordem alfabética

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
#print(c.count(5)) #Quantos números 5 tem em c
print(c.index(2, 4)) #Posição que se encontra o 2, a partir da posição 4
del(a) #Exclui a tupla a. Não é possível deletar um ítem, apenas a tupla inteira
