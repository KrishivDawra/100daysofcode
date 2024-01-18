t=int(input())
for i in range(t):
    s,x,y,z=map(int,input().split())
    d=s-x-y
    if(d>=z):
        print(0)
    else:
        if(s-x>=z or s-y>=z):
            print(1)
        elif(x+y>=z):
            print(2)
