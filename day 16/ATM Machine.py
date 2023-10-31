t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=""
    for j in range(n):
        if(a[j]<=k):
            s=s+'1'
            k=k-a[j]
        else:
            s=s+'0'
    
    print(s)
            
