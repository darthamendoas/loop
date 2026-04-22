novo=0
velho=0
nnovo=""
nvelho=""

for i in range(7):
    idade=int(input("Qual a idade:"))
    nome=str(input("Qual o nome:"))
    if i==0:
        novo=idade
        velho=idade
        nnovo=nome
        nvelho=nome
        continue
    if idade>velho:
        velho=idade
        nvelho=nome
    if idade<novo:
        novo=idade
        nnovo=nome
print(nvelho)
print(velho)
print(nnovo)
print(novo)