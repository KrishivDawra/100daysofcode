t=int(input())
for i in range(t):
    k=s=0
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for j in range(3):
        if(a[j]==1):
            k=k+1
        if(b[j]==1):
            s=s+1
    if(k==s):
        print("Pass")
    else:
        print("Fail")
