t=int(input())
for i in range(t):
    n=int(input())
    k=n
    s=0
    while(n>0):
        a=n%10
        s=s+a
        n=n//10
    
    while(s%2==0):
        k=k+1
        s=0
        n=k
        while(n>0):
            a=n%10
            s=s+a
            n=n//10
    print(k)
        
