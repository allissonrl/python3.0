distancia = int(input('Qual é a distancia da viagem em Km: '))
if distancia <= 200:
    valor = distancia * 0.50
   # print(f'\033[32mO preco da passagem vai custar {valor:.2f} reais\033[m')
else:
    valor = distancia * 0.45
print(f'\033[34mA distancia é {distancia}Km\h e a passagem vai custar {valor:.2f} reais\033[m')