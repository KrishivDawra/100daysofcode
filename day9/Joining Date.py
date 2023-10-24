t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if n%5==0:
        n=n//5
    else:
        n=(n//5)+1
    if k%5==0:
        k=k//5
    else:
        k=(k//5)+1        
    print(n-k)
