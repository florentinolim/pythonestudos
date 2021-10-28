palavra = 'SYSSOA ORA-00001'
with open("messages.txt", 'r') as f:
    f.read().count(palavra)
print('teste'.format(f.read))
mensagem = f.readlines()
for linha in mensagem:
    if palavra in linha:
        print(linha.rstrip())

'''w'ith open(file_path, 'r') as f:
    f.read().count(palavra)'''
