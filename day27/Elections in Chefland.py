t=int(input())
for i in range(t):
    xa,xb,xc=map(int,input().split())
    if(xa>50):
        print("A")
    elif(xb>50):
        print("B")
    elif(xc>50):
        print("C")
    else:
        print("NOTA")
