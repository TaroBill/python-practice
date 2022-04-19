def main():
    a = list(input())
    b = list(input())
    print(trans(a,b,len(a),len(b)))
    
def trans(a,b,c,d):
    # print(a[c-1],b[d-1])
    if(c == 0 or d == 0):            
        return c+d

    elif(a[c-1]==b[d-1]):            #化簡
        return trans(a,b,c-1,d-1)

    elif(a[0]==b[0]):                #化簡
        a.pop(0)
        b.pop(0)
        return trans(a,b,c-1,d-1) 
    
    return min(trans(a,b,c-1,d),trans(a,b,c,d-1),trans(a,b,c-1,d-1))+1
        

if __name__ == "__main__":
    main()