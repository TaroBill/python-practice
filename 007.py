a,b=int(input()),int(input())
x=int(b/2)
def R_Tri():
    for i in range(x):
        print("*"*(i+1))
    if(b%2==1):
        print("*"*(x+1) )
    for i in range(x,0,-1):
        print("*"*(i))
def L_Tri():
    for i in range(x,0,-1):
        print("."*(i)+"*"*(x-(i-1)))
    if(b%2==1):
        print("*"*(x+1) )
    for i in range(x):
        print("."*(i+1)+"*"*(x-(i)))
        
    
def Diam():
    for i in range(x):
        if(x!=1):
            print("."*(x-i) + "*"*((i+1)*2-1))
        else:
            print(".*")
    print("*"*b)
    for i in range(x,0,-1):
        if(x!=1):
            print("."*(x-i+1) + "*"*(2*i-1))
        else:
            print(".*")    
        
if a==1:
    R_Tri()
elif a==2:
    L_Tri()
elif a==3:
    Diam()
        
        
    