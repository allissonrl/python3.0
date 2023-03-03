import cores
reis = float(input('Quantos Reais voce tem? R$'))
dolares = reis / 5.16
Iene = reis * 25.57
print(f'Voce tem {cores.textoverde}R${reis} reais na carteira, e pode comprar {cores.textoazul}{dolares:.2f} dolar {cores.fecha}')
print(f'Voce tem R${reis:.2f}, e pode comprar {Iene:.2f} ienes')
