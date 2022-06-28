import json

#abre o arquivo e transforma o json em um dicionário
conteudo = open('Exercicio 3/dados.json').read()
listaDias = json.loads(conteudo)

#verifica qual o maior e menor faturamento e calcula a média mensal, ignorando-se dias com valor 0
media = 0
total = 0
primeiro = True
for item in listaDias:
  if(item['valor'] != 0):
    if(primeiro == True):
      maior = item['valor']
      menor = item['valor']
      primeiro = False
    elif(item['valor'] > maior):
      maior = item ['valor']
    elif(item['valor'] < menor):
      menor = item['valor']
    
    total += 1
    media += item['valor']
    
media /= total

#verifica em quantos dias o faturamento diário foi maior que o mensal
dias = 0
for item in listaDias:
  if(item['valor'] > media):
    dias += 1
    
print("Menor faturamento diario do mes:", menor)
print("Maior faturamento diario do mes:", maior)
print("Numero de dias do mes em que o faturamento diario superou a media mensal:", dias)