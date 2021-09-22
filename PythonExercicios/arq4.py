import os

#lista apenas os arquivos txt da pasta
pasta = "D:\pythonestudos\PythonExercicios"
caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
arquivos_txt = [arq for arq in arquivos if arq.lower().endswith(".txt")]

#cria uma lista para armazenar as saídas
saida = []

#percorre os arquivos
for arq in arquivos_txt:
  #abre o arquivo
  with open(arq) as f:
      linhas = f.readlines()

  #soma os valores
 # soma = 0
  #for linha in linhas:
    # soma += float(linha.strip().split(" ")[0])

  #guarda na lista de saida
  saida.append("O total por segundo no arquivo {} é: {} \n".format(arquivos_txt,soma))

#grava a lista em um novo arquivo
arq_saida = open('/arquivo_saida.txt', 'w')
arq_saida.writelines(saida)
arq_saida.close()