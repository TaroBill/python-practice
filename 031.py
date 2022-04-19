b = str(input())
listb = b.split(" ")
a = str(input())
lista = a.split(" ")
for i in range(len(lista)):
    lista[i] = int(lista[i])
num = sorted(lista)
for i in range(len(listb)):
    print(listb[lista.index(num[i])],end="")