t=int(input())
for i in range(t):
    a1,a2,a3,a4,a5,p=map(int,input().split())
    l=(a1+a2+a3+a4+a5)*p
    o=120
    if(l>o):
        print("Yes")
    else:
        print("No")
