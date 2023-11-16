def swap(a,b):
    temp=a
    a=b
    b=temp
    

for i in range(int(input())):
    s=input()
    l=list(s)
    c=0
    for i in range(0,len(l)-1):
        if(l[i]=='<' and l[i+1]=='>'):
            c=c+1
    print(c)
