t=int(input())
for i in range(t):
    n,x,y=map(int,input().split())
    s=(n+1)*y
    if(x<=s):
        print("YES")
    else:
        print("NO")
