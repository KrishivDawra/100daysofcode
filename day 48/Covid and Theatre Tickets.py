t=int(input())
for i in range(t):
    k=0
    n,m=map(int,input().split())
    if((m%2)!=0):
        k=m//2
        k=k+1
    else:
        k=m//2
     
    if((n%2)!=0):
        p=n//2
        p=p+1
    else:
        p=n//2   
    
    l=k*p
    print(l)
