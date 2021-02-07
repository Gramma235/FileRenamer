import os

def renameFiles(path,pattern):
    filenum=0
    path+='\\'
    for i in os.listdir(path):
        infilepath=os.path.join(path, i)
        filenum+=1
        splittedname = os.path.splitext(i)
        newname=path+pattern+str(filenum)+splittedname[1]
        os.rename(infilepath, newname)

flag=True
while flag==True:
    path=input("Укажите путь к папке: ")
    pattern=input("Укажите шаблон, по которому нужно переименовывать: ")
    renameFiles(path,pattern)
    continuerunning=input("Хотите переименовать файлы в еще одной папке(напишите 'да' или что-либо другое): ")
    if continuerunning.lower()=='да':
        continue
    else:
        flag=False
