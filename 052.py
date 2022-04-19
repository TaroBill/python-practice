# 1 0 1 1 1 1 1
# 1 0 0 0 1 0 0
# 1 0 1 0 1 0 1
# 1 0 1 0 0 0 1
# 1 1 1 1 1 1 1
row = int(input())
col = int(input())
rows = []
for i in range(row):
    tip = input().split(" ")
    for i in range(col):
        tip[i]=int(tip[i])
    rows.append(tip)
fl = lambda s: False if s[-1]=="x" else True
def Lost2(TL,r,c,d):
    w = TL[r][c]
    up = d + "u"
    down = d + "d"
    left = d + "l"
    right = d + "r"
    x = d+"x"
    if(w==1):
        return x
    if(c==col-1):
        return d
    if(d[-1]=="d"):
        return list(filter(fl,[Lost2(TL, r+1, c, down),Lost2(TL, r, c+1, right),Lost2(TL, r, c-1, left)]))[0] if list(filter(fl,[Lost2(TL, r+1, c, down),Lost2(TL, r, c+1, right),Lost2(TL, r, c-1, left)]))!=[] else "x"
    elif(d[-1]=="u"):
        return list(filter(fl,[Lost2(TL, r-1, c, up),Lost2(TL, r, c+1, right),Lost2(TL, r, c-1, left)]))[0] if list(filter(fl,[Lost2(TL, r-1, c, up),Lost2(TL, r, c+1, right),Lost2(TL, r, c-1, left)])) != [] else "x"
    elif(d[-1]=="l"):
        return list(filter(fl,[Lost2(TL, r-1, c, up),Lost2(TL, r+1, c, down),Lost2(TL, r, c-1, left)]))[0] if list(filter(fl,[Lost2(TL, r-1, c, up),Lost2(TL, r+1, c, down),Lost2(TL, r, c-1, left)])) !=[] else "x"
    elif(d[-1]=="r"):
        return list(filter(fl,[Lost2(TL, r-1, c, up),Lost2(TL, r+1, c, down),Lost2(TL, r, c+1, right)]))[0] if list(filter(fl,[Lost2(TL, r-1, c, up),Lost2(TL, r+1, c, down),Lost2(TL, r, c+1, right)])) != [] else "x"
    return x
print(Lost2(rows, 0, 1,"d")[1:])