for i in range(int(input())):
    n=int(input())
    s=input()
    c=0
    while(c<(len(s)-1)):
        if(s[c]==s[c+1]):
            c+=2
            n-=1
        else:
            c+=1
    print(n)
