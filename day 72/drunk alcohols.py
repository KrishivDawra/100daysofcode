t=int(input())
for i in range(t):
    k=int(input())
    s=0
    for j in range(1,k+1,1):
        if(j%2!=0):
            s=s+3
        else:
            s=s-1
    print(s)
