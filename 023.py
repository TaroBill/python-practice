w = input()
sp = w.split(" ")
A1,An,D = int(sp[0]),int(sp[1]),int(sp[2])
s=0
i=A1
while(i != An):
    print(i,end=" ")
    s+=i
    i+=D
print(An)
s+=An
print(s)