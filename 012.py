def classes(Num,time):
    i=0
    while(i<time):
        Num[i] = int(input())
        i+=1

class1Num,HR1 = int(input()),int(input())
one = [0] * HR1
classes(one,HR1)
class2Num,HR2 = int(input()),int(input())
two = [0] * HR2
classes(two,HR2)
class3Num,HR3 = int(input()),int(input())
three = [0] * HR3
classes(three,HR3)
for y in one:
    for z in two:
        if(y==z):
            print("{0} and {1} confict on {2}".format(class1Num,class2Num,y))
            continue
for y in one:
    for u in three:
        if(y==u):
            print("{0} and {1} confict on {2}".format(class1Num,class3Num,y))
            continue
for z in two:     
    for u in three:        
        if(z==u):
            print("{0} and {1} confict on {2}".format(class2Num,class3Num,z))
            continue