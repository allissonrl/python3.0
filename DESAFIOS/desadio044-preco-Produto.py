import cores

produto = float(input('Qual é o preco do produto: '))
condPagam = 'Condição Pagamento'
print(f'{cores.textoverde}{condPagam:^30}{cores.fecha}',end='')
print("""
        [1]-Dinheiro/Cheque a Vista
        [2]-A vista no Cartão
        [3]-Cartao em 2X
        [4]-Cartao 3x ou mais""")
opcao = int(input('Digite a Opção de Pagamento: '))
if opcao == 1:
    desconto = (produto * 10) / 100
    print(f'O produto é R$ {produto} e tem de desconto R$ {desconto:.2f}'
          f' e ficando R$ {produto - desconto:.2f}')

elif opcao == 2:
    desconto = (produto * 5) / 100
    print(f'O produto é R$ {produto} e tem de desconto R$ {desconto:.2f}'
          f' e ficando R$ {produto - desconto:.2f}')
elif opcao == 3:
    print(f'O valor do produto é R$ {produto} e '
          f' parcelado fica 2X de  R$ {produto/2:.2f}')
elif opcao == 4:
    juros = (produto * 20) / 100
    produtoJuros = produto + juros
    vezes = int(input('Quantas vezes: '))
    parcela = (produto + juros) / vezes
    print(f'O valor do produto é {produto}, parcelado'
          f' em {vezes} X de {parcela:.2f} total de -> {produtoJuros}')
else:
    print('opção errada, tente novamente!')
    print(f'A sua compra ficou {produto}')