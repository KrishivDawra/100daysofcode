t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    if(a>=b):
        b=b+c
    else:
        a=a+c
    
    if(a>=b):
        b=b+d
    else:
        a=a+d
    
    if(a>=b):
        print("N")
    else:
        print("S")
