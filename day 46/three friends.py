t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    print("yes" if a+b==c or b+c==a or a+c==b else "no")
