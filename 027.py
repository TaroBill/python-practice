x= int(input())
l = []
long = []
for i in range(x):
    a= str(input())
    ranges= a.split(" ")
    ranges[0] = int(ranges[0])
    ranges[1] = int(ranges[1])
    for j in range(ranges[0],ranges[1]):
        long.append(j)
l = list(set(long))
print(len(l))