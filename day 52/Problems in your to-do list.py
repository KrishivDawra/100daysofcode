t=int(input())
for i in range(1,t+1,1):
    n=int(input())
    d=list(map(int,input().split()))
    s=0
    for j in range(0,n,1):
        if(d[j]<1000):
            s=s+1
    n=n-s
    print(n)
