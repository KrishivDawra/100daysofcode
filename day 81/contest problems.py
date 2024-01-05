t=int(input())
for i in range(t):
    n=int(input())
    l=tuple(map(str,input().split()))
    s=d=0
    for j in range(n):
        if(l[j]=="START38"):
            s=s+1
        else:
            d=d+1
    print(s,d)
  
