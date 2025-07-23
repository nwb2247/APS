P = int(input())
for _ in range(P) :
    T, *lst = list(map(int, input().split()))
    cnt = 0
    for i in range(20) :
        j = 0
        while j < i :
            if lst[j] > lst[i] :
                cnt += i-j
                lst[j:i+1] = sorted(lst[j:i+1])
                break
            j += 1
    print(T, cnt)
    