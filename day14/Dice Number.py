t=int(input())
for i in range(t):
    l = list(map(str, input().split(' ')))
    a = []
    a.append(l[0])
    a.append(l[1])
    a.append(l[2])
    b = []
    b.append(l[3])
    b.append(l[4])
    b.append(l[5])
    a.sort(reverse = True)
    b.sort(reverse = True)
    a = int(a[0] + a[1] + a[2])
    b = int(b[0] + b[1] + b[2])
    if(a > b): 
        print("Alice")
    elif(a < b): 
        print("Bob")
    else:
        print("Tie")
