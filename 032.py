a = str(input())
lista = a.split(" ")
l1,m =[],[]
reserve = []
ccc=-2
for i in range(len(lista)):
    lista[i] = int(lista[i])
x = list(set(lista))
num = []
for i in range(len(x)):
    num.append(lista.count(x[i]))
x1 = list(num.copy())
num = sorted(num,reverse=True)
st = x.copy()
st1 = x1.copy()
if(num[0]<=sum(num[1:])):
    for i in range(len(lista)):
        for j in range(len(l1)):
        #    print(l1)
            if(lista[i]<l1[j] and lista[i] != l1[j-1]):
                l1.insert(j,lista[i])
                break
            try:
                if(lista[i]>l1[j] and lista[i] < l1[j+1]):
                    l1.insert(j+1,lista[i])
                    break
            except:
                l1.insert(j+1,lista[i])
                break
            if(lista[i]==l1[j]):
                continue
        else:
            try:
                if(l1[0]==0):
                    l1[0]=0
            except:
                l1.append(lista[i])
                continue
            if(lista[i] == l1[-1]):
                reserve.append(lista[i])
            else:
             #   print("append: ",end = "")
                l1.append(lista[i])
             #   print(l1)
    for i in reserve:
        for j in range(len(l1)):
           # print(l1)
            if(i<l1[j] and i != l1[j-1]):
                l1.insert(j,i)
                break
            try:
                if(i>l1[j] and i < l1[j+1]):
                    l1.insert(j+1,i)
                    break
            except:
                l1.insert(j+1,i)
                break
            if(i==l1[j]):
                continue
        else:
            if(i == l1[-1] and l1[ccc-1]!=l1[-1]):
                l1.insert(ccc,i)
                ccc-=2
            elif(l1[ccc-1]==l1[-1]):
                ccc-=2
                reserve.append(i)
            else:
              #  print("append: ",end = "")
                l1.append(i)
               # print(l1)
else:
    for k in range(0,len(num)):
        if(x[k] == st[st1.index(num[0])]):
            continue
        for j in range(lista.count(x[k])):
            l1+=str(st[st1.index(num[0])])+str(x[k])
    l1+=str(st[st1.index(num[0])])
    for i in range(len(l1)):
        l1[i] = int(l1[i])
for i in l1 :
    print(i,end="")