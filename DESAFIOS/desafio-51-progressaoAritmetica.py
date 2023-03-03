primeiro = int(input('primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro +(10-1) * razao
for c in range(primeiro,decimo+razao, razao):
    print(f'{c}')
print('Acabou')