import calendar
import cores
from datetime import date
ano = int(input('que ano quer analizar? digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
    print(f'Ano atual é {ano}')
if calendar.isleap(ano):
    print(f'{cores.textociano}ele é bissexto{cores.fecha}')
else:
    print(f'{cores.textoazul}não é bissexto{cores.fecha}')