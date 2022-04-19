count=int(input())
s=[[]]*count
for i in range(count):
    x=input().split(",")
    s[i]=range(int(x[0]),int(x[1])+1)
for i in range(len(s)):
    for j in s:
        L1=list(j)
        L2=list(s[i])
        if((set(j)&set(s[i])!=None) and j!=s[i] and (set(j)&set(s[i])!=set())):
            if(L2[0] in L1 and L2[-1] in L1):
                s.append(range(L1[0],L1[-1]+1))
            elif(L1[-1] in L2 and L1[0] in L2):
                s.append(range(L2[0],L2[-1]+1))
            elif(L2[0] in L1):
                s.append(range(L1[0],L2[-1]+1))
            elif(L2[-1] in L1):
                s.append(range(L2[0],L1[-1]+1))
            s[s.index(j)]=[]
            s[i]=[]
        elif(j==s[i] and s.index(j)!=i):
            s[i]=[]            
for i in range(s.count([])):#remove掉空陣列
    s.remove([])
for i in range(len(s)):
    for j in s:
        L1=list(j)
        L2=list(s[i])
        if((set(j)&set(s[i])!=None) and j!=s[i] and (set(j)&set(s[i])!=set())):
            if(L2[0] in L1 and L2[-1] in L1):
                s.append(range(L1[0],L1[-1]+1))
            elif(L1[-1] in L2 and L1[0] in L2):
                s.append(range(L2[0],L2[-1]+1))
            elif(L2[0] in L1):
                s.append(range(L1[0],L2[-1]+1))
            elif(L2[-1] in L1):
                s.append(range(L2[0],L1[-1]+1))
            s[s.index(j)]=[]
            s[i]=[]
        elif(j==s[i] and s.index(j)!=i):
            s[i]=[]     
for i in range(s.count([])):#remove掉空陣列
    s.remove([])
for i in range(len(s)):#將range型態轉成list
    s[i]=list(s[i])
    s[i]=[s[i][0],s[i][-1]]
for i in range(len(s)-1): #泡沫排序
    for j in range(len(s)-i-1):
        if(s[j][0]>s[j+1][0]):
            s[j],s[j+1]=s[j+1],s[j]
for i in s:
    print(str(i[0])+","+str(i[1]))