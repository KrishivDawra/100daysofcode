t=int(input())
for i in range(1,t+1,1):
    a,b=map(int,input().split())
    s=a+b
    if(s%2==0):
        print("Bob")
    else:
        print("Alice")
