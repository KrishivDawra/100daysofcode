import math
t=int(input())
for _ in range(t):
    l,r,m = (map(int,input().split()))
    k=math.ceil(m / l)
    s=math.floor(m / r)
    d=k+s
    print(d)
