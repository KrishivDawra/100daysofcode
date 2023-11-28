for i in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=sorted(a)
    ans="YES"
    moves=0
    for x in range(len(a)):
        if a[x]!=b[x]:
            if x==len(a)-1:
                ans="NO"
            else:
                a[x],a[x+1]=a[x+1],a[x]
                moves+=1
    if moves>1:
        ans="NO"
    print(ans)
