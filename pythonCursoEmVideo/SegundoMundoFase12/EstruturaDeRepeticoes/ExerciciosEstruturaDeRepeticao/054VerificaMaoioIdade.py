#Crie um programa que leia o ano de nascimento de 7 pessoas.
# No final mostre quantas pessoas ainda não atigiram a maior idade
#E quantos já são maiores
s = 0
from datetime import date
for n in range(0, 7):
    AnoNasc = int(input('Digite o ano de nascimento: '))
    Anoatual = date.today().year
    IdadeAtual = Anoatual - AnoNasc
    if IdadeAtual >= 21:
        p = 1
        s += p
        print('Atingiu a MAIOR IDADE, você tem {} anos de idade'.format(IdadeAtual))
    elif IdadeAtual < 21:
        print('Não atingiu a MAIOR IDADE, você tem {} anos de idade'.format(IdadeAtual))
print('Numero de pessoas MAIOR IDADE SÃO: {}'.format(s))
print('Numero de pessoas MENOR IDADE SÃO: {}'.format(s))
