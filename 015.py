string = str(input())
big=0
for i in string:
    if(i.islower()):
        print(i,end="")
    elif(i.isupper()):
        big+=1
print("")
if((len(string)-big) ==0):
    print("No lowercase letters")
print(len(string))
print(big)
        