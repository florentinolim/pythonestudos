from datetime import date
atual = date.today().day
palavra = 'SYSSOA ORA-00001'
import os
path = "D:\pythonestudos\PythonExercicios"
os.chdir(path)
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        f.read().count(palavra)
print('O numerous de ocorrências {:.3f} no arquivo messages '.format(f.read)) # num de vezes que a palavra aparece