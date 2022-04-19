A,B = input(),input()
if(len(A)==len(B)):
    print(len(A))
else:
    if((len(A)-len(B))>0):
        print(len(A))
        print(B,end="")
        for i in range(abs(len(A)-len(B))):
            print("a",end="")
    else:
        print(len(B))
        print(A,end="")
        for i in range(abs(len(A)-len(B))):
            print("a",end="")        
            