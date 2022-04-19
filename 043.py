num = int(input())
sx=[""]*num
spx=[[]]*num
d={}
for i in range(num):
    sx[i]=str(input())
    spx[i]=sx[i].split(" ")
    d.setdefault(i,0) 
lupsidedown=[]
s = str(input())
sp = s.split(" ")
for string in sp:    #先從搜尋第一個字開始
    string = string.lower() #轉小寫
    for sxtring in range(len(sx)):#第幾行字串
        for spxlit in range(len(spx[sxtring])):#此字串被空白split
            spxlit2 = spx[sxtring][spxlit].lower()
            if(string in spxlit2):  #如果搜尋的字在被空白split裡
                d[sxtring]+=1
                spx[sxtring][spxlit] = (spxlit2.replace(string,string.upper()))#轉成大寫
            else:
                spx[sxtring][spxlit] = spx[sxtring][spxlit]#原本的格式輸出(防止前面轉小寫轉到)
for x in range(len(sx)):
    sx[x] = " ".join(spx[x])#合併split
for key,value in d.items():
    lupsidedown.append([value,key])
lupsidedown = sorted(lupsidedown,reverse=True)
ok=False
for ik in range(len(lupsidedown)-1):
    if(not ok):
        temp=[]
    if(lupsidedown[ik][0] == lupsidedown[ik+1][0]):
        temp.append(sx[lupsidedown[ik][1]])
        ok=True
        continue
    elif(ok):
        temp.append(sx[lupsidedown[ik][1]])
        temp.sort()
        for k in range(len(temp)):
            sx[lupsidedown[ik-(len(temp)-k-1)][1]]=temp[k]
        ok=False
if(ok):
    temp.append(sx[lupsidedown[ik+1][1]])
    temp.sort()
    for k in range(len(temp)):
        sx[lupsidedown[ik+1-(len(temp)-k-1)][1]]=temp[k]
    ok=False
for i in lupsidedown:
    print(sx[i[1]])
         