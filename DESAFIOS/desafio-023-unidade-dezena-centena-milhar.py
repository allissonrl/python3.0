import cores
num = int(input('digite um numero entre 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'{cores.textoazul}unidade = {u}\n{cores.textamarelo}dezena = {d}\n{cores.textoverde}centena = {c}\n{cores.textociano}milhar = {m} {cores.fecha} ')

