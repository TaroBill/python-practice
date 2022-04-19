# 1 0 1 1 1 1 1 1 1 1
# 1 0 0 0 0 0 1 0 0 1
# 1 1 0 1 1 1 1 1 0 1
# 1 1 0 0 0 0 0 0 0 1
# 1 1 1 0 1 0 1 1 1 1
# 1 1 1 0 1 0 0 0 0 1
# 1 0 0 0 1 1 1 1 0 1
# 1 0 1 1 1 0 0 0 0 0
# 1 0 0 0 0 0 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
row = int(input())
col = int(input())
rows = []
dp =[[0]*col]*row
for i in range(row):
    tip = input().split(" ")
    for i in range(col):
        tip[i]=int(tip[i])
    rows.append(tip)
fl = lambda s: False if s==100000 else True
def Lost2(TL,r,c,d,step):
    step +=1
    w = TL[r][c]
    up = d + "u"
    down = d + "d"
    left = d + "l"
    right = d + "r"
    if(w==1):
        return 100000
    if(c==col-1):
        # print(d)
        return step
    if(step >= (col*row/2)):
        return 100000    
    L2L = Lost2(TL, r, c-1, left,step) if dp[r][c-1] ==0 else dp[r][c-1]
    L2R = Lost2(TL, r, c+1, right,step) if dp[r][c+1] ==0 else dp[r][c+1]
    L2U = Lost2(TL, r-1, c, up,step) if dp[r-1][c] ==0 else dp[r-1][c]
    L2D = Lost2(TL, r+1, c, down,step) if dp[r+1][c] ==0 else dp[r+1][c]
    if(d[-1]=="d"):
        return min(list(filter(fl,[L2D,L2R,L2L]))) if list(filter(fl,[L2D,L2R,L2L]))!=[] else 100000
    elif(d[-1]=="u"):
        return min(list(filter(fl,[L2U,L2R,L2L]))) if list(filter(fl,[L2U,L2R,L2L])) != [] else 100000
    elif(d[-1]=="l"):
        return min(list(filter(fl,[L2U,L2D,L2L]))) if list(filter(fl,[L2U,L2D,L2L])) !=[] else 100000
    elif(d[-1]=="r"):
        return min(list(filter(fl,[L2U,L2D,L2R]))) if list(filter(fl,[L2U,L2D,L2R])) != [] else 100000
    return 100000
print(Lost2(rows, 0, 1,"d",0)-1)