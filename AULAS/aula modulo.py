"""
import bebidas=> vai importar todas as bebidas
from bebidas import cafe => vai importar só o café

IMPORT no começo, importa tudo
from bebidas import cafe => vai importar só um elemento

             import match
CEIL = arrendondamento para cima
FLOOR = arrendondamento para baixo
TRUNC = vai eliminar da virgula, sem arrendondar
POW = potencia **
SQRT = raiz quadrada
FACTORIAL = calcula fatorial

usando uma importacao
FROM MATCH IMPORT ....
"""
import math
import emoji
print(emoji.emojize('Ola, mundo :two_hearts:'))
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} e igual a {raiz}')
     #  OU
from math import sqrt, floor
num1 = int(input('digite um numero: '))
raiz1 = sqrt(num)
print(f'A raiz de {num} é igual a {floor(num1):.3f}')