store={}
storeList=[]
storeSum=int(input())
for i in range(storeSum):
    shop=input()
    store[shop]=0
    storeList.append(shop)
VoteP=int(input())
for i in range(VoteP):
    index=int(input())
    store[storeList[index-1]]+=1
Most=""
for key in store:
    if(Most==""):
        Most=key
    elif(store[key]>store[Most]):
        Most=key
print(Most,store[Most])