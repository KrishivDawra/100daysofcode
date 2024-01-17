n=int(input())
a=list(map(int,input().split()))
k=s=0
for i in range(0,n,1):
    if(a[i]%2==0):
        k=k+1
    else:
        s=s+1
if(k>s):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
