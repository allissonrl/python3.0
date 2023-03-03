import cores

km = float(input('Quantos KM percorridos? '))
diasAlugados = int(input('Quantos dias alugados? '))
valorDiaCarro = diasAlugados * 60
kmRodado = km * 0.15
valorTotal = valorDiaCarro + kmRodado
print(f'O valor a pagar é de R$ {cores.textovermelho} {valorTotal:.2f} {cores.fecha}')