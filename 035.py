def SGCD(x,y):
    l1,l2=[],[]
    for i in range(1,len(x)+1):
        if(x.replace(x[:i],"")==""):
            l1.append(x[:i])   
    for i in range(1,len(y)+1):
        if(y.replace(y[:i],"")==""):
            l2.append(y[:i])
    l1.extend(l2)
    if(sorted(list(set(l1)))==sorted(l1)):
        return "No GCD"
    for i in set(l1):
        l1.remove(i)
        maxs=l1[0]  
    for i in l1:
        if(len(maxs)<len(i)):
            maxs=i
    return(maxs)
while(True):
    x = input().split(" ")
    if(x[0]=="-1"):
        break
    else:
        print(SGCD(x[0],x[1]))
        