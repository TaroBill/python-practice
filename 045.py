word1 = list(input())
word2 = list(input())
lenw2 = len(word2)
temp=""
tmpL= []
tmpx=0
def twoW(word1,word2):
    if(word1 == word2):
        return 0
    for i in range(lenw2):
        for j in range(i+1,lenw2):
            word1t = word1.copy()
            if(word2[i] in word1 and word2[j] in word1[word1.index(word2[i]):]):
                if(word1.index(word2[j],word1.index(word2[i])) - word1.index(word2[i],word1.index(word2[i])) >= j-i):
                    temp = word2[i]+word2[j]
                    tmpx=j
                    for x in range(j+1,lenw2):
                        if(word2[x] in word1[word1.index(word2[j]):]):
                            if(word1.index(word2[x],word1.index(word2[x])) - word1.index(word2[j],word1.index(word2[i])) >= (x-j)):
                                   temp+=word2[x]
                                   tmpx=x
                            else:
                                break
                        else:
                            break
                    while(word1t.count(word2[i])>1 and word1t.index(word2[i],word1t.index(word2[i])) < word1t.index(word2[tmpx],word1t.index(word2[i]))):
                        word1t[word1.index(word2[i],word1.index(word2[i]))]= "*"
                    tmpL.append([temp,word1t.index(word2[i],word1t.index(word2[i])),word1t.index(word2[tmpx],word1t.index(word2[i])),i,tmpx])
                    temp=""
    for i in range(0,len(tmpL)-1): #有n-1回合(n為數字個數)
        for j in range(0,len(tmpL)-1-i): #每回合進行比較的範圍
            if len(tmpL[j][0]) < len(tmpL[j+1][0]): #是否需交換
                tmpL[j], tmpL[j + 1] = tmpL[j + 1], tmpL[j]
            elif len(tmpL[j][0]) == len(tmpL[j+1][0]):
                if(tmpL[j][2]-tmpL[j][1] > tmpL[j+1][2]-tmpL[j+1][1]):
                    tmpL[j], tmpL[j + 1] = tmpL[j + 1], tmpL[j]                
    print(tmpL)
    if(tmpL != []):
        long = len(word1) - len(tmpL[0][0])
        while(long<(len(word1)-1)):
            if(word2[0] not in tmpL[0][0] and tmpL[0][1]==0):
                long+=1
                word2 = word2[1:]
            elif(word2[-1] not in tmpL[0][0] and (len(word1)-(tmpL[0][2]+1) < len(word2)-(tmpL[0][4]+1))):
                long+=1
                word2 = word2[:-1]
            else:
                break        
        return long 
    else:
        for i in word1:
            for j in word2:
                if i == j:
                    break
            if i == j:
                return len(word1)-1
                break
        else:
            return len(word1)
print(twoW(word1,word2))