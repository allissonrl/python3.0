from datetime import date
anoAtual = date.today().year
nascimento = int(input('qual o seu ano de nascimento: '))
idade = anoAtual - nascimento
print(f'A sua idade {idade}')
if idade <= 9:
    print(f'A sua idade é {idade} anos e voce esta na categoria Mirim')
elif 9 < idade <= 14:
    print(f' a sua idade é {idade} anos e voce esta categoria infantil')
elif idade <= 19:
    print(f'a sua idade é {idade} anos e voce esta na categoria Junior')
elif idade <= 25:
    print(f'Sua idade é {idade} anos e voce esta na categoria Senior')
else:
    print(f'A sua idade é {idade} anos e voce esta categoria Master')