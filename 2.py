codigo=0
while codigo!=-1:
    codigo=int(input("Qual o código"))
    if codigo==1:
        print("Um")
    elif codigo==2:
        print("Dois")
    elif codigo==3:
        print("Tres")
    elif codigo==-1:
        break
    else:
        print("Codigo invalido")