t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=0
    for j in range(n):
        s=1
        for k in range(j+1,n,1):
            if(a[j]==a[k]):
                s=s+1
        if(s>=m):
            m=s
    
    n=n-m
    print(n)
