t=int(input())
for i in range(t):
    n,v1,v2=map(int,input().split())
    s=(n*2**0.5)/v1
    e=(2*n)/v2
    
    if(s<=e):
        print("Stairs")
    else:
        print("Elevator")
