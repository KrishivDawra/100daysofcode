t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    for j in range(1,11,1):
        d1=10*(j-1)+1
        d2=10*j
        if(x>=d1 and x<=d2):
            l=j
            break
    
    for j in range(1,11,1):
        d1=10*(j-1)+1
        d2=10*j
        if(y>=d1 and y<=d2):
            k=j
            break
    
    if(k>=l):
        s=k-l
    else:
        s=l-k
    print(s)
