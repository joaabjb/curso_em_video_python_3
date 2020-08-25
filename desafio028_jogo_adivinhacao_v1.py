import random
num = random.randint(0,5)
n = int(input('Adivinhe o número inteiro escolhido entre 0 e 5: '))
print('Você venceu' if num==n else f'Você perdeu, o número escolhido foi {num}')

