t=int(input())
for i in range(t):
    n,a=map(int,input().split())
    s=n-a
    if(s<=a):
        print(s)
    else:
        print(a)
      
