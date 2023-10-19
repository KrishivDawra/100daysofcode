t=int(input())
for i in range(t):
    H,x,y,C=map(int,input().split())
    s=x+(y//2)
    a=s*H
    if(a<=C):
        print("YES")
    else:
        print("NO")
