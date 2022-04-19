def isContinue(l):
    l = sorted(l)
    for i in range(len(l)-1):
        # print(l[i]+1,l[i+1])
        if(l[i]+1 != l[i+1] and l[i]+9 != l[i+1]):
            return False
    return True
def same(l):
    l = sorted(l)
    d={}
    for i in range(len(l)):
        if(l[i] in d):
            d[l[i]]+=1
        else:
            d[l[i]]=1
    temp=[]
    #print(d)
    for key,value in d.items():
        if(value>1):
            temp.append([key,value])
    return temp
def main():
    ip = input()
    ip = ip.replace("A","14")
    ip = ip.replace("J","11")
    ip = ip.replace("Q","12")
    ip = ip.replace("K","13")
    poke = ip.split(" ")
    number=[]
    color=[]
    for i in range(5):
        if(poke[i][1].isdigit()):
            number.append(int(poke[i][0]+poke[i][1]))
            color.append(poke[i][2])
        else:
            number.append(int(poke[i][0]))
            color.append(poke[i][1])
    SN=same(number)
    #print(color,number,SN)
    if(isContinue(number) and same(color)[0][1]==5):
        print(8)
    elif(same(color)[0][1]==5):
        print(5)        
    elif(isContinue(number)):
        print(4)
    elif(SN==[] and not isContinue(number)):
        print(0)
    elif(SN[0][1]==4):
        print(7)

    elif(len(SN)>1):
        if(SN[0][1]>=2 and SN[1][1]==5-SN[0][1]):
            print(6)
        elif(SN[0][1]==2):
            print(2)
    elif(SN[0][1]==3):
        print(3)
    elif(SN[0][1]==2):
        print(1)
main()