t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    e=o=0
    for j in range(n):
        if(a[j]%2==0):
            e=e+a[j]
        else:
            o=o+a[j]
    if(o%2==0 and o>0):
        print("YES")
    else:
        print("NO")
