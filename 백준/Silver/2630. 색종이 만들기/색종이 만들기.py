"""
[조건]
N = 2^k <= 128
4개로 잘라서 모두 같은 색이 아니라면 또 4등분

[목표]
파란 종이와 하얀 종이의 수

[접근]
분할 정복
모두 같은 색이면 분할 X
다른 색이면 2개로 나눠봄

~(size//2) -1 | size//2 로 나누자

더 이상 쪼갤 수 없는 1*1의 사이즈는 바로 반환
"""

def recur(sr, sc, size):

    if size == 1:               # 종료 조건 (사이즈가 1*1)
        if arr[sr][sc] == 1:    # 파란색
            return 0, 1
        else:                   # 하얀색
            return 1, 0

    # 1의 갯수를 셈
    cnt = 0
    for r in range(sr, sr + size):
        for c in range(sc, sc + size):
            cnt += arr[r][c]
    if cnt == size*size:    # 파란색
        return 0, 1
    elif cnt == 0:          # 하얀색
        return 1, 0
    else:                   # 다 같은 색이 아니라면 분할, 병합
        sw, sb = 0, 0
        for i in [sr, sr+size//2]:
            for j in [sc, sc+size//2]:
                w, b = recur(i, j, size//2)
                sw += w
                sb += b
        return sw, sb



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
w, b = recur(0, 0, N)
print(w)
print(b)
