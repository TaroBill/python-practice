s = str(input())
c=[]
cc=[]
N=0
def fab(n):
    if(n==0):
        return 1
    elif(n==1):
        return 2
    else:
        return fab(n-1)+fab(n-2)
def loop(a):
    tmp=1
    for i in a:
        tmp*=fab(i)
    return tmp
ok=True
for n in range(len(s)-1):
    if(not ok):
        cc[N]-=1
        if(cc[N]<=0):
            ok=True
            N+=1
        continue     
    if((s[n]=="2" and int(s[n+1])<7) or s[n]=="1"):
        c.append(1)
        cc.append(1)
        for i in range(n+1,len(s)-1):
            if((s[i]=="2" and int(s[i+1])<7) or s[i]=="1"):
                c[N] +=1
                cc[N] +=1
            elif(s[i]=="0"):
                c[N]-=1
                cc[N]-=1
                break
            else:
                break
        ok=False
if((not ok) and s[-1]=="0"):
    c[-1]-=1
    if(c[-1]>0):
        c[-1]-=1
    else:
        c[-1]=0
calcu=loop(c)
print(calcu)