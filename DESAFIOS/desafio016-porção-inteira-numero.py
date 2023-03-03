from math import trunc
import cores
num = float(input('Digite um numero Real: '))
porçãoInteira = trunc(num)
print(f'O numero {cores.textoazul} {num} {cores.fecha} e a sua porção inteira é {cores.textoverde} {porçãoInteira} {cores.fecha}')