t=int(input())
for i in range(t):
    e,k=map(int,input().split())
    d=e//k
    s=1
    while(d>0):
        s=s+1
        d=d//k
    print(s)
