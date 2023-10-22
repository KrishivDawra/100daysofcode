t=int(input())
for i in range(t):
    x=int(input())
    s=0
    while(x>=0):
        if(x%10==0):
            print(s)
            break
        else:
            x=x*2
            if(x%10!=0):
                print(-1)
                break
            s=s+1
