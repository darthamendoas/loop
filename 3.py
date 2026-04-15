x=int(input("Escolha um numero:"))
y=int(input("Escolha outro numero:"))
if x>y:
    for i in range(y+1,x):
        print(i,end=" ")
elif x<y:
    for i in range(x+1,y):
        print(i,end=" ")
else:
    print("Escolha números diferentes")