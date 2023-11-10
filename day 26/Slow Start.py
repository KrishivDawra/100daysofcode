t=int(input())
for i in range(t):
    x, h = map(int,(input().split()))
    t = 0
    while(h>0):
        if(t<5):
            h=h-(x//2)
        else:
            h=h-x 
        t=t+1
    print(t)
    
