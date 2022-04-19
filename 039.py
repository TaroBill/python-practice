Messages={}
messageSum=int(input())
for i in range(messageSum):
    M = input().split(" ",1)
    Messages[int(M[0])]=M[1]
readTimeTimes=int(input())
for i in range(readTimeTimes):
    time= int(input())
    if(Messages.get(time)==None):
        Messages[time]="-.---.-----.-.-........-.."
    else:
        Messages[time+0.5]="-.---.-----.-.-........-.."
Messages={K:Messages[K] for K in sorted(Messages.keys())}
tmp="-.---.-----.-.-........-.."
#tmp=""
c=0
for key in Messages.keys():
    if(c==messageSum):
        break
    elif(tmp=="-.---.-----.-.-........-.." and Messages[key]=="-.---.-----.-.-........-.."):
        continue
    if(Messages[key]=="-.---.-----.-.-........-.."):
        print("-")
    else:
        print(Messages[key]) 
    if(Messages[key]!="-.---.-----.-.-........-.."):
        c+=1     
    tmp=Messages[key]
        