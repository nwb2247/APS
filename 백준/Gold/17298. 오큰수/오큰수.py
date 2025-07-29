def solve():
    N = int(input())
    lst = list(map(int, input().split()))
    stk = []
    ans = [-1]*N
    for i in range(N-1,-1,-1):
        # 오큰수가 나올 때까지 pop
        while len(stk) != 0 and stk[-1] <= lst[i]:
            stk.pop()
        # stk이 비어있지 않다면 (즉, 오큰수가 존재한다면)
        if len(stk) != 0:
            ans[i] = stk[-1]
        # 이번엔 자기 자신을 stk에 넣음
        stk.append(lst[i])
    print(*ans)

solve()
