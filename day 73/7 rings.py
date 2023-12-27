for i in range(0,t,1):
    n,x=map(int,input().split())
    c=n*x
    c=str(c)
    d=len(c)
    if(d==5):
        for j in range(0,1,1):
            if(c[j]=='0'):
                print("NO")
            else:
                print("YES")
    else:
        print("NO")
