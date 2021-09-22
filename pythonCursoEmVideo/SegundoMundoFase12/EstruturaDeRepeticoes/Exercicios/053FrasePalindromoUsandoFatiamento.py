#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
#Ex: APOS A SOPA
#A SACADA DA CASA
#A TORRE DA DERROTA
#O LOBO AMA O BOLO
#ANOTARAM A DATA DA MARATONA
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[:: -1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindomo!')
else:
    print('A frase digitada não é um palindromo!')    
