def solve():
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()

    mn = 0
    mx = 0
    for num in lst:
        if mn + num <= mx+1:
            mn = min(mn, num)
            mx = mx + num
        else:
            print(mx + 1)
            break
    else:
        print(mx + 1)

solve()