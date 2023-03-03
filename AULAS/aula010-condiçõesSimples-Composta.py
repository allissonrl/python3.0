#"A ORDEM É SEMPRE DE CIMA PARA BAIXO => UM CAMINHO"

#"CRIACAO DE POSSIBILIDADES => CONDIÇÕES"
  #                "Ccarro.siga()"
#"se carro.esquerda()"
 #     "carro.siga()"
  #   "carro.direita()"
#   "carro.siga()"
 #  "carro.direita()"
  #      "carro.esquerda()"
   #     "carro.siga()"
    #    "carro.direita()"
     #   "carro.siga()"
#"senão"
 #       "carro.siga()"
  #      "carro.esquerda()"
  #      "carro.siga()"
  #      "carro.esquerda"
  #      "carro.siga()"
  #                         "carro.pare()"

  #if carro.esquerda():
   #   print('verdadeira')                 => " CONDIÇÃO, É EXECUTADO UM OU OUTRO"
  #else:
   #   print("falso")

#tempo = int(input('Quanto tempo tem o seu carro? '))
# OU pode se usado assim print('carro novo' if tempo< = 3 else 'carro velho')

#if tempo <= 3:
 #   print('seu carro é novo')
#else:
#    print('seu carro é velho')
#print('--FIM--')

#nome = str(input('Qual é o seu nome: ')).strip().lower()
#if nome == 'allisson':
 ##   print('Que nome lindo')
##elif 'allisson' in nome:
##    print('voce tem nome e sobreno')
##else:
 #   print('Que nome comum')
#print(f'Bom dia, {nome}')


n1 = float(input('digite a primeiro nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1+n2) / 2
print(f'A sua media foi {m:.1f}')
if m <= 5.9:
    print('Nota abaixo da media')
else:
    print('Nota na media')