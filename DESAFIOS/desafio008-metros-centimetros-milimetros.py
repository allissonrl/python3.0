textovermelho = '\033[31m'
textoverde = '\033[32m'
textamarelo = '\033[33m'
textoazul = '\033[34m'
textociano = '\033[36m'
verdesubliando = '\033[4;32m'
fundoAzul = '\033[44m'
fecha = '\033[m'

metros = float(input('Digite uma medida em metros: '))
quilomentro = metros/1000
hectometro = metros/100
decametro = metros/10

decimetro = metros*10
centimetro = metros * 100
milimetros = metros * 1000
print(f' O tamanho tem{textoazul} {metros}m, {decimetro}{fecha} dm \n {textovermelho}{centimetro} cm, \n {milimetros} mm {fecha}')
print(f' O tamanho tem {textamarelo} {metros}m, {decametro}da,{textoazul} {hectometro}hm, {quilomentro}km {fecha}')
