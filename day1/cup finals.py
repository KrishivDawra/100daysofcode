t=int(input())
for i in range(1,t+1,1):
    x,y,d=map(int,input().split())
    if(x>=y):
        s=x-y
    else:
        s=y-x
    if(s<=d):
        print("YES")
    else:
        print("NO")
