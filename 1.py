impar=0
par=1
for i in range(1,30,2):
    impar+=i
for i in range(2,31,2):
    par*=i
print("Multiplicação dos pares",par)
print("Soma dos impares",impar)
