t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=0
    for j in a:
        m=max(a.count(j),m)
    print(n-m)
