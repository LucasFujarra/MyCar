#consumo de combustivel por Km/h  1.0
import time
import replit

print('================================= \n==============MyCar==============\n=============================1.0= \n')
time.sleep(2)
replit.clear()

set = 1
while set == 1 : 
  set = 0
  print("==============MyCar==============")
  preco = input('  Digite o preço do combustivel \n  (ex. 4,25)\n================================= \n::> ')
 
  replit.clear()
  print("==============MyCar==============")
  consumo = input(' Insira o consumo médio\n do veículo por litro \n > https://combustivel.app/#home <\n================================= \n::> ')
  replit.clear()
  print("==============MyCar==============")
  distancia = input('  Digite a distancia em Km \n================================= \n::> ')
  replit.clear()

  #tratamento de caracter
  p = preco.replace(",", ".")
  c = consumo.replace(",", ".")
  d = distancia.replace(",", ".")
  
  #transforma string em float
  precof = float(p)
  consumof = float(c)
  distanciaf = float(d)

  #processamento de dados 
  consumoTotal = distanciaf / consumof
  valorTotal = consumoTotal * precof

  #sainda de dados
  print("==============MyCar==============")
  print(f' Seu veículo percorrerá {distancia} km \n Gastando {round(consumoTotal , 2)} Litros \n No preço de  {round(valorTotal , 2)} R$')
  print("=================================")
  set = int (input('Deseja executar novamente \n 1) sim \n 2) não \n================================= \n::>'))
  replit.clear()




