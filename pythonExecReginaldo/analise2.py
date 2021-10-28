#!/usr/bin/env python
# -*- coding: utf-8 -*-
arq = open('messages.txt', 'r')
texto = arq.readlines()
x = 0
Saida = ""
for linha in texto:
    Array = linha.split()
    if x != 1:
      print("data                  id")
      x+=1
    if (len(Array) == 7 and Array[0] == '-e'):
      Saida += Array[2] + ' ' + Array[3] + ' ' + Array[4]
    if (len(Array) > 7 and Array[14] in Array and Array[14] != 'id'):
      Saida += ',      ' + Array[14] + "\n"
print(Saida)
arq.close()