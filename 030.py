a = str(input())
lista = a.split(" ")
for i in range(len(lista)):
    lista[i] = int(lista[i])
x = sorted(lista)
l1=[]
l2=[]
for i in x:
    if(i%2==0):
         l1.append(i)
    else:
        l2.append(i)
l2.extend(l1[::-1])
print(l2)