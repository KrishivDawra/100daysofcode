t=int(input())
for i in range(t):
    x=int(input())
    str=input()
    c=n=d=0
    l=len(str)
    for j in range(l):
        if(str[j]=='C'):
            c=c+1
        elif(str[j]=='N'):
            n=n+1
        else:
            d=d+1
    if(c>n):
        f=x*60
    elif(c==n):
        f=x*55
    else:
        f=x*40
        
    print(f)
