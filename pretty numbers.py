t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    s=0
    for j in range(l,r+1,1):
        p=j%10
        if(p==2 or p==3 or p==9):
            s=s+1
    print(s)
