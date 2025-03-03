import math
n = float(input('Digite o ângulo que você deseja: '))
rad = math.radians(n)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'''O ângulo de {n} tem o SENO de {sen:.2f}
O ângulo de {n} tem o COSSENO de {cos:.2f}
O ângulo de {n} tem a TANGENTE de {tan:.2f}''')
