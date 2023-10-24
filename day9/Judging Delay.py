t=int(input())
for i in range(t):
    n=int(input())
    k=0
    for j in range(1,n+1,1):
        s,j=map(int,input().split())
        j=j-s
        if(j>5):
            k=k+1
    print(k)
