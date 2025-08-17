"""
F_n+1   = [1 1] [F_n]
F_n     = [1 0] [F_n-1]
(F_n+1 = F_n + F_n-1 / F_n = F_n)

=>


"""
from collections import defaultdict


def mul(a, b):
    ret = [[0] * 2 for _ in range(2)]
    for r in range(2):
        for c in range(2):
            for m in range(2):
                ret[r][c] += (a[r][m] * b[m][c] % M)
            ret[r][c] %= M
    return ret


def recur(n):
    if n == 1:
        return A

    if not DP[n]:
        tmp = recur(n // 2)
        if n % 2 == 0:
            DP[n] = mul(tmp, tmp)
        else:
            DP[n] = mul(mul(tmp, tmp), A)
    return DP[n]


N = int(input())
A = [[1, 1], [1, 0]]
DP = defaultdict(lambda: [])
M = 1000000007
print(recur(N)[0][1])
