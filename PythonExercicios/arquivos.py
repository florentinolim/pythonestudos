import os
path = "D:\pythonestudos\PythonExercicios"
os.chdir(path)
palavra = 'SYSSOA ORA-00001'
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print('O numero de ocorrências de erros do {} é {:.2f}'.format(palavra, f.read().count(palavra)))
for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
        read_text_file(file_path)
