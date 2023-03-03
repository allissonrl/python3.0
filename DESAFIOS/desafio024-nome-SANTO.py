cidade = input('digite o nome de uma cidade: ').strip()
nomeSAnto = (f'{cidade[0:5].upper()}')
nomeSAnto1 = "SANTO" in nomeSAnto

print(f'A cidade {cidade} tem nome santo =>  {nomeSAnto1}')