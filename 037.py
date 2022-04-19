FS= input()
SS = input()
A=[]
for i in range(len(FS)):
    for y in range(i,len(FS)+1):
        k=FS[i:y]
        for j in SS:
            if j not in k:
                break
            else:
                k=k.replace(j,"",1)
        else:
            A.append(FS[i:y])
mins=A[0]
for i in A:
    if(len(i)<len(mins)):
        mins=i
print(mins)