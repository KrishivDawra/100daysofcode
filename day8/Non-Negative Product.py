t=int(input())
for i in range(t):
    n=int(input())
    k=0
    s=1
    a=list(map(int,input().split()))
    for j in range(n):
        s=s*a[j]
    if(s>=0):
        print(k)
    else:
        print(1)
