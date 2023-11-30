import math
for i in range(int(input())):
    coins=int(input())
    res=int((math.sqrt(1+8*coins)-1)//2)
    print(res)
