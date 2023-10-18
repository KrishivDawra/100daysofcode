t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    s=0
    for j in range(n):
        if(a[j]<=b[j]):
            if((2*a[j])>=b[j]):
                s=s+1
        else:
            if(a[j]<=(2*b[j])):
                s=s+1
    print(s)      
