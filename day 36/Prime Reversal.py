for i in range(int(input())):
    n = int(input())
    a = str(input())
    b = str(input())
    if a.count('0')==b.count('0') and a.count('1')==b.count('1'):
        print("YES")
    else : print("NO")
