ip = str(input())
d = dict()
l = list()
for char in ip:
    if(char in d and not char.isdigit()):
        d[char] += 1 
    elif(char!=" "):
        d[char]=1
        l.append(char)
#print(d)
for i in l:
    if(i.isdigit()):
        print(i,end="")
    elif(d[i]<10):
        print(d[i],end="")