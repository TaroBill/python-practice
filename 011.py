X = [0]*3
Y = [0]*3
for i in range(3):
    X[i] = input()
    if(X[i]=="A"):
        X[i] = 1
    elif(X[i] == "J"or X[i] == "Q" or X[i] == "K"):
        X[i] = 0.5
    else:
        X[i] = int(X[i])        
for i in range(3):
    Y[i] = input()
    if(Y[i]=="A"):
        Y[i] = 1
    elif(Y[i] == "J"or Y[i] == "Q" or Y[i] == "K"):
        Y[i] = 0.5
    else:
        Y[i] = int(Y[i])  
A1 = X[0] + X[1] + X[2]
A2 = Y[0] + Y[1] + Y[2]
if(A1>10.5):
    A1=0
if(A2>10.5):
    A2=0   
print(A1)
print(A2)
if(A1>A2):
    print("A贏")
elif(A1<A2):
    print("B贏")
else:
    print("平手")
