t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for j in range(n):
        p=1
        s=0
        for k in range(j,n):
            s=s+a[k]
            p=p*a[k]
            if(s==p):
                c=c+1
    print(c)
