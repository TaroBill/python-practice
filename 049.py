# 1 2 3 4 5 6 7 8 9
# 2 3 4 5 6 7 8 9 1
# 3 4 5 6 7 8 9 1 2
# 4 5 6 7 8 9 1 2 3
# 5 6 7 8 9 1 2 3 4
# 6 7 8 9 1 2 3 4 5
# 7 8 9 1 2 3 4 5 6
# 8 9 1 2 3 4 5 6 7
# 9 1 2 3 4 5 6 7 8
def three(ln):
    c=0
    ltmp=[0]*3
    for i in range(len(ln)):
        ltmp[c]+=ln[i]
        if(i%3==2):
            c+=1          
    return ltmp
def NineNine(l):
    d={}
    for i in l:
        for y in i:
            if(y in d):
                d[y]+=1
            else:
                d[y]=1
    for values in d.values():
        if(values !=9):
            return "No"
    lf=[]
    tmp=0
    for i in range(9):
        tmp=0
        for y in range(len(l)):
            tmp+=l[y][i]
        if(tmp!=45):
            return False
    for i in l:
        if(sum(i)!=45):
            return "No"
    for i in range(len(l)):
        l[i] = three(l[i])
    # print(l)
    for i in range(3):
        lt=[]
        for y in range(len(l)):
            lt.append(l[y][i])
        lf.append(three(lt))
    for i in lf:
        for y in i:
            if(y !=45):
                return "No"
    return "Yes"
def main():
    l=[[]]*9
    for i in range(9):
        l[i]=input().split(" ")
    for i in range(len(l)):
        for k in range(len(l[i])):
            l[i][k] = int(l[i][k])
    print(NineNine(l))
main()