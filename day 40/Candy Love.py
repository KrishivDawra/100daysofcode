t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    for j in range(n):
        s=s+a[j]
    if((s%2)!=0):
        print("YES")
    else:
        print("NO")
