import cores
prod = float(input('Qual é o valor do produto: R$ '))
desc = prod - (prod * 5) / 100
print(f'O preço do produto é R$ {cores.textoverde} {prod} reais, com desconto de 5% fica R$ {cores.textovermelho} {desc:.2f} reais {cores.fecha}')