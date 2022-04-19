m,n=int(input()),int(input())
sums=0
sumsum=1
for i in range(m,n+1,2):
    sums +=i
for i in range(m,n+1,3):
    sumsum *=i
print(sums)
print(sumsum)
    