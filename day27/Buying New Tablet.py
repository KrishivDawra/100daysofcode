t=int(input())
for i in range(t):
    n,b=map(int,input().split())
    a1=0
    d=0
    for j in range(n):
        w,h,p=map(int,input().split())
        a=w*h
        if(a>a1):
            if(p<=b):
                a1=a
                d=1
    if(d==1):
        print(a1)
    else:
        print("no tablet")
         
