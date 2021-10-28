#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import *
# dia   mes   ano   horario
#  28    03   2017  20:17:01
#  %d    %m   %Y    %X
def retornaResultado(DataInicio, DataFinal):
  arq = open('messages.txt', 'r')
  Inicio = int(datetime.strptime(DataInicio, '%d %m %Y %X').timestamp())
  Final  = int(datetime.strptime(DataFinal,  '%d %m %Y %X').timestamp())
  texto = arq.readlines()
  x = 0
  Saida = ""
  DataArquivo = ""
  for linha in texto:
      Array = linha.split()
      if x != 1:
        print("data                  id")
        x+=1
      if (len(Array) == 7 and Array[0] == '-e'):
        DataArquivo = int(datetime.strptime(Array[3] + ' ' + Array[2] + ' ' + Array[6] + ' ' + Array[4],  '%d %b %Y %X').timestamp())
        if DataArquivo >= Inicio and DataArquivo <= Final:
          Saida += Array[2] + ' ' + Array[3] + ' ' + Array[4]
      if (len(Array) > 7 and Array[14] in Array and Array[14] != 'id'):
        if DataArquivo >= Inicio and DataArquivo <= Final:
          Saida += ',      ' + Array[14] + "\n"
  print(Saida)
  arq.close()