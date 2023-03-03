import cores
from math import radians, tan, sin, cos
num = float(input('Qual é o angulo: '))
seno = sin(num)
cosseno = cos(num)
tangente = tan(num)
print(f'O angulo é {num}, ')
print(f'{cores.textoverde}seu seno è {seno:.2f},{cores.textoazul} seu cosseno é {cosseno:.2f},{cores.textamarelo} e o tangente è {tangente:.2f}{cores.fecha}')
