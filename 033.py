def fib(n):
    if(n==1):
        return 1
    elif(n==2):
        return 1
    else:
        return fib(n-1) +fib(n-2)
while(True):
    x = int(input())
    if(x==-1):
        break
    else:
        print(fib(x))