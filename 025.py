x= int(input())
s=""
i=2
for i in range(2,x+1):
    while(x%i==0):
        x /= i
        s+= str(i)+"*"
print(s[0:-1])