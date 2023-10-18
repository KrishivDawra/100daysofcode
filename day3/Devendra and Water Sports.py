t=int(input())
for i in range(1,t+1,1):
    z,y,a,b,c=map(int,input().split())
    s=z-y
    if(s>=(a+b+c)):
        print("YES")
    else:
        print("NO")
