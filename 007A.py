A,B,x,y= input(),input(),input(),input(),
C = A+B
D = C.replace(x,y)
length = len(C) + len(D)
E = D[:3:1] + D[-3::1]
print(length)
print(E*3)