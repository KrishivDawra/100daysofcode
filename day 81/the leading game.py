n=int(input())
x=c=0
e1=e2=0
for i in range(n):
    p1,p2=map(int,input().split())
    x=x+p1
    c=c+p2
    if(x>=c):
        s=x-c
        if(s>=e1):
            e1=s
    else:
        d=c-x
        if(d>=e2):
            e2=d

if(e1>=e2):
    print(1,e1)
else:
    print(2,e2)
