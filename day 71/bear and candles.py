t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    p=1
    s=2
    d=o=0
    for j in range(0,a,):
        if(p<=a):
            a=a-p
            d=d+p
            p=p+2
        else:
            break
        
    for k in range(0,b,):
        if(s<=b):
            b=b-s
            o=o+s
            s=s+2
            
        else:
            break
    if(d>=o):
        print("Limak")
    else:
        print("Bob")
