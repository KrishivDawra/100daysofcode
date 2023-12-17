t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    p=max(a)
    o=max(b)
    d=s=0
    for j in range(0,n,1):
        d=d+a[j]
        s=s+b[j]
    d=d-p
    s=s-o
    if(d>s):
        print("Bob")
    elif(d==s):
        print("Draw")
    else:
        print("Alice")
