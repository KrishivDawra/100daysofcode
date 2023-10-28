t=int(input())
for i in range(t):
    n,k=map(int, input().split())
    x= k*(k+1)//2
    if n>=x:
        print('YES')
    else:
        print("NO")
