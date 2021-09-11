#Faça um programa que calcule a soma entre todos os numeros impáres que são
# Multiplos de três a que se encontram no intervalo de 1 até 500.
s =0
for n in range(0, 500, 3):
    m: int = n + 3
 #   print(m)
    s += m
print('{:.1f}'.format(s))

print('Fim')

