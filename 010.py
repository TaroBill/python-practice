A,B,C,X,Y,Z=30,70,40,int(input()),int(input()),int(input())
def money(M,Num,H20,H15,H10):
    if(Num>20):
        M = M*H20
        return M
    elif(Num>15):
        M = M*H15
        return M
    elif(Num>10):
        M = M*H10
        return M
    else:
        return M
u = money(A,X,0.8,0.9,0.95)
m = money(B,Y,0.75,0.85,0.9)
r = money(C,Z,0.8,0.8,0.85)
z = u*X+m*Y+r*Z
if(X+Y+Z)>=30:
    z *=0.87

print(int(z))