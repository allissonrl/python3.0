from math import hypot
import cores
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto Adjacente: '))
hi = hypot(co,ca) # tambem assim -> hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'O cateto Oposto é {cores.textoverde} {co} e o cateto adjacente é {cores.textoazul} {ca} \nA sua hipotenusa é {cores.textamarelo} {hi:.2f} {cores.fecha}')