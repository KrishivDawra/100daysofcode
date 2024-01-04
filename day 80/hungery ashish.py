t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x>=y:
        print('PIZZA')
    elif x>=z:
        print('BURGER')
    else:
        print("NOTHING")
