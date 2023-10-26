t=int(input())
for i in range(t):
    s=input()
    l=len(s)
    a=b=0
    for j in range(0,l,1):
        if(s[j]=='a'):
            a=a+1
        else:
            b=b+1
    if(b<=a):
        print(b)
    elif(b==0 or a==0):
        print(0)
    else:
        print(a)
