t=int(input())
for i in range(t):
    d=int(input())
    k=0
    n=input()
    l=len(n)
    for j in range(l):
        if(n[j]=='0' or n[j]=='5'):
            k=1
    if(k==1):
        print("YES")
    else:
        print("NO")
