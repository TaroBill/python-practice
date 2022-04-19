S1Amount = int(input())
S1 = input().split(" ")
setS1 = set()
for i in range(S1Amount):
    setS1.add(S1[i])
op = input()
S2Amount = int(input())
S2 = input().split(" ")
setS2 = set()
for i in range(S2Amount):
    setS2.add(S2[i])
if(op=="&"):
    A = setS1 & setS2
elif(op=="|"):
    A = setS1 | setS2
elif(op=="-"):
    A = setS1 - setS2
elif(op=="^"):
    A = setS1 ^ setS2
elif(op==">"):
    A = setS1 > setS2
elif(op=="<"):
    A = setS1 < setS2
elif(op==">="):
    A = setS1 >= setS2
elif(op=="<="):
    A = setS1 <= setS2
elif(op=="=="):
    A = setS1 == setS2
if(not("<" in op or ">" in op or "=" in op)):
    A=str(sorted(A))
    A= "{"+A[1:-1]+"}"
print(A)