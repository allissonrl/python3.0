frase = str(input('Digite uma frase: ')).strip().upper()
contA = frase.count('A')
posicao1 = frase.find('A')
ultimaposicao = frase.rfind("A")
print(f'A letra A aparece {contA} vezes')
print(f'A letra A esta na {posicao1+1} posicão')
print(f'A letra A aparece ultima vez na posição {ultimaposicao+1}')