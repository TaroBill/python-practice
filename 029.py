def findMod(j,k,l):
    p=j*k
    i=1
    r=0
    while(r!=1):
        p=j*k
        p*=i
        r = (p)%l
        i+=1
    else:
        return p
A = input()
x = A.split(" ")
for i in range(len(x)):
    x[i] = int(x[i])
f = findMod(x[2],x[4],x[0])*x[1]+findMod(x[4],x[0],x[2])*x[3]+findMod(x[0],x[2],x[4])*x[5]
g = x[0]*x[2]*x[4]
print(f%g)