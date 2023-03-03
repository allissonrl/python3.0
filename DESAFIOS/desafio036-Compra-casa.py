import cores
valorCasa = float(input('Qual é o valor da casa: '))
salario = float(input('Qual é o seu Salario: '))
anos = int(input('Quantos meses vai pagar: '))
prestacao = valorCasa / anos
if prestacao > (salario*30) /100:
    print(f'A prestacao da casa é R$ {prestacao:.2f}')
    print(f'{cores.textovermelho}FINANCIAMENTO NEGADO{cores.fecha}')
    print(f'{cores.textoazul}O valor da parcela ultrapassa 30% do salario{cores.fecha}')
elif prestacao < (salario*30) / 100:
    print(f'A prestacao da casa é R$ {prestacao:.2f}')
    print(f'{cores.textoverde}finaciamento APROVADO{cores.fecha}')