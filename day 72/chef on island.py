t=int(input())
for i in range(t):
    x,y,xr,yr,d=map(int,input().split())
    s=x/xr
    f=y/yr
    if(s<=f):
        if(s>=d):
            print("YES")
        else:
            print("NO")
    else:
        if(f>=d):
            print("YES")
        else:
            print("NO")
