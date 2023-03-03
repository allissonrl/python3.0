import cores
salario = float(input('digite o salario do funcionario: '))
if salario > 1250:
    aumento10 = (salario * 10)/100
    print(f'O seu aumento de salario é {aumento10}, total de R$ {salario + aumento10:.2f}')
if salario <= 1250:
    aumento15 = (salario * 15)/100
    print(f'{cores.textociano}O seu aumento de salario é {aumento15} total de R$ {salario + aumento15:.2f}{cores.fecha}')
