t=int(input())
for i in range(t):
    a1,a2=map(int,input().split())
    b1,b2=map(int,input().split())
    c1,c2=map(int,input().split())
    s1=a1+a2
    s2=b1+b2
    s3=c1+c2
    if(s1>=s2 and s1>=s3):
        print(s1)
    elif(s2>=s1 and s2>=s3):
        print(s2)
    elif(s3>=s1 and s3>=s2):
        print(s3)
