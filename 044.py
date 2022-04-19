s = str(input())
l = []
keep="k"
n=-1
sums=0
for i in s:
    if(i.isnumeric()):
        if(keep.isnumeric()):
            l[n]+=i
        else:
            l.append(i)
            n+=1
    keep=i
for i in l:
    sums+=int(i[::-1])
print(sums)
    