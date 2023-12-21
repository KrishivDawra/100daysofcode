if __name__ == '__main__':
    l1=[]
    t=int(input())
    for _ in range(t):
        name = input()
        score = float(input())
        l=[]
        l.append(name)
        l.append(score)
        l1.append(l)
    
    p=[]
    for i in range(t):
        p.append(l1[i][1])
    
    
    d=min(p)
    for i in range(t):
        if(l1[i][1]==d):
            p.remove(l1[i][1])
    d=min(p)
    
    m=[]
    for i in range(t-1,-1,-1):
        if(l1[i][1]==d):
            m.append(l1[i][0])
    m.sort()
    for i in range(len(m)):
        print(m[i])
