invo,outvo,phone,inLine,outLine = int(input()),int(input()),int(input()),int(input()),int(input())
A = [0] * 3
A[0] = invo * 0.08 + outvo * 0.1393 + phone * 0.1349 + inLine * 1.1287 + outLine * 1.4803
A[1] = invo * 0.07 + outvo * 0.1304 + phone * 0.1217 + inLine * 1.1127 + outLine * 1.2458
A[2] = invo * 0.06 + outvo * 0.1087 + phone * 0.1018 + inLine * 0.9572 + outLine * 1.1243
if(A[0]<183):
    A[0]=183
if(A[1]<383):
    A[1]=383
if(A[2]<983):
    A[2]=983

x = A[0]
for i in range(3):
    if(x>A[i]):
        x=A[i]
if x==A[0]:
    print("183型")
elif x==A[1]:
    print("383型")
elif x==A[2]:
    print("983型")