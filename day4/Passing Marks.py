T=int(input())
for i in range(T):
    a,b,c,t,A,B,C=map(int,input().split())
    if(A>=a and B>=b and C>=c):
        if((A+B+C)>=t):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
