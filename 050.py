d = {}
l=[]
for i in range(26):
    d[10+i] = chr(97+i)
def base(a,b):
   p = a % b
   t = a//b
   l.append(p)
   if(t>0):
       base(t,b)
ip = int(input())
ip2 = int(input())
base(ip,ip2)
for i in range(len(l)):
    if(l[i]>9):
        l[i]= d[l[i]]
    else:
        l[i]=str(l[i])
st = "".join(l)
print(st[::-1])
   