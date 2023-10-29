t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if(n%4==0):
        if(k==1):
            print("On")
        else:
            print("Off")
    elif(k==0):
        print("On")
    else:
        print("Ambiguous")
        
