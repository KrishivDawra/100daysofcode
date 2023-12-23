def swap_case(s):
    l=len(s)
    s1=""
    for i in range(l):
        if(s[i].islower()):
            s1=s1+s[i].upper()
        elif(s[i].isupper()):
            s1=s1+s[i].lower()
        else:
            s1=s1+s[i]
    return s1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
