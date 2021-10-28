ref_arquivo = open("messages.txt","r")
linha = ref_arquivo.readline()
while linha:
    valores = linha.split()
    print('QB ', valores[0], valores[1], 'obteve a avaliacao ', valores[5] )
    linha = ref_arquivo.readline()

ref_arquivo.close()
