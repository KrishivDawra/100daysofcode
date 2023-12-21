if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x=list(student_marks.keys())
    p=list(student_marks.values())
    for i in range(n):
        if(query_name==x[i]):
            s=sum(p[i])
            l=len(p[i])
            d=s/l
            print("{:.2f}".format(d))
