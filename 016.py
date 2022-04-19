N = int(input())
largest = 0
sec= 0
small=1000000000
for i in range(N):
    k=int(input())
    if(k>largest):
        sec = largest
        largest = k
    if(k<small):
        small = k
print(sec)
print(small*largest)