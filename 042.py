d=dict()
d[10000000] =input()
d[2000000] = input()
x=input().split(" ")
d[200000] = {0:x[0],1:x[1],2:x[2]}
head = {3:200,4:1000,5:4000,6:10000,7:40000,8:200000}
special = input().split()
d[200]= {0:special[0],1:special[1],2:special[2]}
num=int(input())
money=0
def mm(s):
    if(s==d[10000000]):
        return 10000000
    elif(s==d[2000000]):
        return 2000000
    for value in d[200000].values():
        for index in range(6):            
            if(value[index:]==s[index:]):
                return head[8-index]
    for value in d[200].values():      
        if(value ==s[-3:]):
            return 200
    return 0
for i in range(num):
    s = input()
    money+=mm(s)
print(money)