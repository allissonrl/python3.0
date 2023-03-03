import cores
temp = float(input('Informe a temperatura m ºC: '))
fahrenheit = temp * 9/5 + 32 # ordem de precendencia
# f = 9 * temp / 5 + 32 ou assim tambem
print(f'A temperatura de {cores.textoazul} {temp}ºC corresponde a {cores.textovermelho} {fahrenheit}ºF {cores.fecha}')
