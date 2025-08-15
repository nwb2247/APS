def mul(x, y):
    ret = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for i in range(N):
                ret[r][c] += x[r][i]*y[i][c]
            ret[r][c] %= 1000
    return ret

def recur(t):
    if not DP[t]:
        mat2 = recur(t // 2)
        if t%2 == 0:
            DP[t] = mul(mat2, mat2)
        else:
            DP[t] = mul(mul(mat2, mat2), mat)

    return DP[t]


from collections import defaultdict

"""
각 원소가 1000보다 작거나 같은데
1000으로 나눈 나머지를 출력해야함
3 3
1000 1000 1000
1000 1000 1000
1000 1000 1000
등으로 입력이 오는 경우 미리 나눠주고 시작해야함
"""

N, B = map(int, input().split())
mat = [list(map(lambda x:int(x)%1000, input().split())) for _ in range(N)] # 1000으로 나눠주고 시작
DP = defaultdict(list)
DP[1] = mat
ret = recur(B)
for lst in ret:
    print(*lst)