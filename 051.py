# 0 3 1 2 9
# 7 3 4 9 9
# 1 7 5 5 3
# 2 3 4 2 5
row = int(input())
col = int(input())
rows = []
for i in range(row):
    tip = input().split(" ")
    for i in range(col):
        tip[i]=int(tip[i])
    rows.append(tip)
def Lost(TL,r,c,t,step):
    t += TL[r][c]
    # print(r,c)
    step+=1
    if(step>=row*col):
        return 100000
    if(r==row-1 and c == col-1):
        return t
    elif(r==row-1):
        return Lost(TL,r,c+1,t,step)
    elif(c==col-1):
        return Lost(TL,r+1,c,t,step)
    
    return min((Lost(TL,r,c+1,t,step),Lost(TL,r+1,c,t,step)))
print(Lost(rows,0,0,rows[0][0],0))