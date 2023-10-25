t=int(input())
for i in range(t):
    s=k=0
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    for j in range(n):
        if(a[j]<x):
            k=j+1
    print(k)
