if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    s=max(arr)
    d=-111
    for i in range(n):
        if(arr[i]>=d and arr[i]<s):
            d=arr[i]
    print(d)
