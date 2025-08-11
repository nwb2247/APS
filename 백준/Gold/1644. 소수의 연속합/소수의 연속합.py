def solve():
    N = int(input())

    if N == 1:
        print(0)
        return

    lst = [1]*(N+1)
    prime = []
    for i in range(2, N+1):
        if lst[i] == 1:
            prime.append(i)  # 소수를 찾아 넣어줌
            for j in range(i+i, N+1, i):
                lst[j] = 0

    # 투포인터로 합이 N과 일치되는 경우의 수를 세어줌
    s, e = 0, 0
    cnt = 0
    sm = 2
    while True:
        if sm < N:  # 작다면 e늘려줌
            e += 1
            if e >= len(prime): # 범위 벗어나면 break
                break
            sm += prime[e]
        elif sm > N:            # 크다면 s 올려줌
            sm -= prime[s]
            s += 1
        else:                   # 같다면 cnt += 1하고 s 올려줌
            cnt += 1
            sm -= prime[s]
            s += 1

    print(cnt)

solve()

