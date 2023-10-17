
t=int(input())
for i in range(1,t+1,1):
    a1,a2,a3,a4,a5,a6,a7=map(int,input().split())
    s=0
    r=0
    if(a1==0):
        s=s+1
    else:
        r=r+1
        
    if(a2==0):
        s=s+1
    else:
        r=r+1
        
    if(a3==0):
        s=s+1
    else:
        r=r+1
        
    if(a4==0):
        s=s+1
    else:
        r=r+1
        
    if(a5==0):
        s=s+1
    else:
        r=r+1
        
    if(a6==0):
        s=s+1
    else:
        r=r+1
    
    if(a7==0):
        s=s+1
    else:
        r=r+1
        
    if(r>s):
        print("YES")
    else:
        print("NO")
        
    
