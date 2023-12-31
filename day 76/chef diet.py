t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    d=0
    s=0
    for j in range(0,n,1):
        l=a[j]+s
        if((l)>=k):
            d=1
            p=l
            s=p-k
           
        else:
            f=j+1
            d=0
            break
    
    if(d==1):
        print("YES")
    else:
        print("NO",f)
        
