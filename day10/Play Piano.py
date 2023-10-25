t=int(input())
for i in range(t):
    s=input()
    a=b=0
    l=len(s)
    for j in range(0,l,2):
        if(s[j]=='A' and s[j+1]=='B'):
            a=1
        elif(s[j]=='B' and s[j+1]=='A'):
            a=1
        else:
            a=0
            break
    if(a==0):
        print("no")
    else:
        print("yes")
