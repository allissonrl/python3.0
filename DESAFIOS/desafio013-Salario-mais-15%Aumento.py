"""salario = float(input('Qual é o valor do Salario: '))
aumento =salario + (salario * 15) / 100
print(f'O salario atual é R$ {salario} reais, com o aumento de 15% fica R$ {aumento:.2f} reais')"""
import cores
produto = str(input('Qual é o produto: '))
valor = float(input('Qual é o valor do produto: R$'))
valorAvista= valor - (valor * 15 / 100)
parcelado = valor + (valor * 8 / 100)
print(f' O {produto} custa {cores.textoazul} {valor}, a vista {cores.textociano} R${valorAvista}, {cores.fecha} parcelado em 8X fica {cores.textovermelho} R${parcelado} {cores.fecha}')