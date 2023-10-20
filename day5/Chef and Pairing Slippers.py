t=int(input())
for i in range(t):
    n,l,x=map(int,input().split())
    n=n-l
    if(n>=l):
        s=l*x
    else:
        s=n*x
    print(s)
