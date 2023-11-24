t=int(input())
for i in range(t):
    n=int(input())
    b=input()
    s=0
    for j in range(n):
        if(b[j]=='1'):
            s=s+1
    d=120-n
    d=d+s
    avg=(d/120)*100
    if(avg>=75.0):
        print("YES")
    else:
        print("NO")
