t=int(input())
liat=[]
for i in range(t):
    s=0
    k=0
    a=list(map(int,input().split()))
    
    for j in range(0,10,1):
        if(j%2==0):
            if(a[j]==1):
                s=s+1
        else:
            if(a[j]==1):
                k=k+1
    if(s>k):
        print(1)
    elif(s==k):
        print(0)
    else:
        print(2)
