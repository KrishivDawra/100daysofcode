t=int(input())
for i in range(1,t+1,1):
    x,y,z=map(int,input().split())
    s=y-x
    if(s<=(z*2)):
        print("YES")
    else:
        print("NO")
