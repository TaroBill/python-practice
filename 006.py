str,P,Q=input(),input(),input()
sent1 = str.split(" ")
sent2 = str.split(" ")
sent3 = str.split(" ")
ans1 = ''
ans2 = ''
ans3 = ''
for i in sent1:
    if(i==P):
        i=Q
    ans1 += i+" "
for i in sent2:
    if(i==P):
        i = Q + " " + P
    ans2 += i+" "
for i in sent3:
    if(i==P):
        i = ""
        continue
    ans3 += i+ " "
print(ans1)
print(ans2)
print(ans3)