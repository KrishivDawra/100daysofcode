t=int(input())
for i in range(t):
    n=int(input())
    s=0
    a=list(map(int,input().split()))
    for j in range(n-1):
        if(a[j]==a[j+1]):
            n=n-1
    print(n)
