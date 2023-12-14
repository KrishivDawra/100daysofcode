# cook your dish here
t=int(input())
for i in range(t):
    pa,pb,qa,qb=map(int,input().split())
    if(pa>=pb):
        if(qa>=qb):
            if(pa>qa):
                print("Q")
            elif(pa==qa):
                print("TIE")
            else:
                print("P")
        else:
            if(pa>qb):
                print("Q")
            elif(pa==qb):
                print("TIE")
            else:
                print("P")
    else:
        if(qa>=qb):
            if(pb>qa):
                print("Q")
            elif(pb==qa):
                print("TIE")
            else:
                print("P")
        else:
            if(pb>qb):
                print("Q")
            elif(pb==qb):
                print("TIE")
            else:
                print("P")
        
