count=0
palavra = 'SYSSOA ORA-00001'
with open ('messages.txt','rb') as f:
    for line in f:
        count +=1

print(count)