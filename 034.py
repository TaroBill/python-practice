def GCD(x, y):
    if y==0:
        return x
    else:
        return GCD(y, x%y)
while(True):
    x = input().split(" ")
    for i in range(len(x)):
        x[i]=int(x[i])
    if(x[0]==-1):
        break
    else:
        print(GCD(GCD(x[0],x[1]),x[2]))
        