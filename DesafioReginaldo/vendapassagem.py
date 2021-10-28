'''Construa um programa que faça venda de passagens aereas:
1 - Considere que o avião possua 220 lugares.
2 - No horário das 18h até as 22h o cliente terá 10% de desconto
3 - Para cada passgem vendida deverá conter:
Nome do passageiro
Data de nascimento
Documento de identidade
Cpf
Endereço
Telefone
'''
totc = 0
while True:
    qtd = int(input('Numero de passageiros: '))
    origem = str(input('Origem')).strip()
    destino = str('Destino').strip()
    dtida = int(input('Data da ida: ')).strp()
    dtvolta = int(input('Data da volta'))
    nome = str(input('Nome do passageiro: ')).strip()
    endereco =str(input('Endereço: ')).strip()
    tel = str(input('Telefone: ')).strip()
    dtnasc = str(input('Data de nascimento: ')).strip()
    identidade = str(input('Identidade')).strip()
    cpf = str(input('Cpf')).strip()

    totc += qtd
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Deseja continuar comprando S/N')).strip().upper()[0]
    if resp == 'N':
        break
print(totc)





