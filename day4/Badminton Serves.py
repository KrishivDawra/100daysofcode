t=int(input())
for i in range(t):
    p=int(input())
    if(p%2==0):
        s=p//2
        print(s+1)
    else:
        s=(p+1)//2
        print(s)
