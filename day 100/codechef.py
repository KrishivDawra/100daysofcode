t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    o = a = 0
    c = 0
    for i in A:
        if i:
            c += 1
        else:
            c = 0
        o = max(o,c)
    c = 0
    for i in B:
        if i:
            c += 1
        else:
            c = 0
        a = max(a,c)
    if o>a:
        print("Om")
    elif o<a:
        print("Addy")
    else:
        print("Draw")
