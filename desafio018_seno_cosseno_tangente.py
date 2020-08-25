from math import radians, sin, cos, tan

ang = int(input('Digite a medida do ângulo em graus: '))

ang_rad = radians(ang)

print(f'O seno de {ang} é {sin(ang_rad):.3f}')
print(f'O cosseno de {ang} é {cos(ang_rad):.3f}')
print(f'A tangente de {ang} é {tan(ang_rad):.3f}')