t = int(input())
for i in range(t):
    x = int(input())
    y = 0
    while(x>0):
        s = x%10
        if (s == 4):
            y = y+1
        x = x//10
    print(y)
