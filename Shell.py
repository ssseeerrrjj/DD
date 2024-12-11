import os
curdir = os.getcwd()
while(1):
    command = input().split()
    if(len(command) == 1):
        if(command[0] == "pwd"):
            print(os.getcwd())
        elif(command[0] == "ls"):
            print(os.listdir())
        else:
            print("syntax error")
    elif(len(command) == 2):
        if(command[0] == "cd"):
            nextdir = command[1].replace("(","").replace(")","")
            try:
                os.chdir(nextdir)
            except(NotADirectoryError):
                print(f"{nextdir} не является директорией")
            except(FileNotFoundError):
                print(f"Файл {nextdir} не найден")
