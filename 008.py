string = input()
a= True
abc=False
lists = []
while a:
    f=input()
    if(f!="0"):
        lists.append(f)
    else:
        a=False
sent = string.split(" ")
for c in sent:
    for x in lists:
        if c==x:
            abc = True
            break
    if(abc==True):
        print(c,end=" ")
        abc=False
    else:
        print(c[::-1],end=" ")

