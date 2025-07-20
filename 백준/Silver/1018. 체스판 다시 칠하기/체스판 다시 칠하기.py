import sys, math

mat1 = ["WBWBWBWB", "BWBWBWBW"]*4
mat2 = ["BWBWBWBW", "WBWBWBWB"]*4

N, M = map(int, sys.stdin.readline().split())
strs = [sys.stdin.readline().rstrip() for _ in range(N)]

sol = math.inf

for i in range(N-8+1) :
    for j in range(M-8+1) :
        cnt1 = 0
        cnt2 = 0
        for a in range(0, 8) :
            for b in range(0, 8) :
                if mat1[a][b] != strs[i+a][j+b] : cnt1 += 1
                if mat2[a][b] != strs[i+a][j+b] : cnt2 += 1
        sol = min(sol, min(cnt1, cnt2))
print(sol)

