from datetime import date
import  cores
anoatual = date.today().year
anoNascimento = int(input('Qual e o seu ano de nascimento: '))
idade = anoatual - anoNascimento
print(f'Voce tem {idade} anos')

if idade < 18:
    saldo = 18 - idade
    print(f'Falta {idade - 18} anos para voce se alistar.')
    print(f'Seu alistamento sera em {saldo}')
elif idade == 18:
    print(f'Voce tem {idade} esta na hora de se alistar')
elif idade > 18:
    saldo = idade - 18
    print(f'A sua idade é {idade} anos e passou {cores.textovermelho}{idade-18} anos tempo do alistamento{cores.fecha}')
    print(f'Seu alistamento foi {saldo}')