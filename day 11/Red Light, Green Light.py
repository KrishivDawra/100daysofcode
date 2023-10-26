t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=0
    a=list(map(int,input().split()))
    l=len(a)
    for j in range(0,l,1):
        if(a[j]>k):
            s=s+1
    print(s)
