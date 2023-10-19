n=int(input())
s=0
while(n>0):
    n=n//10
    s=s+1
if(s==1):
    print("1")
elif(s==2):
    print("2")
elif(s==3):
    print("3")
else:
    print("More than 3 digits")
