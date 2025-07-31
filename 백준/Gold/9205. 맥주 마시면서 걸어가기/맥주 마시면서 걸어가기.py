from collections import deque

M = 20*50 # 1병당 50미터 이므로 한번 충전후 최대 1000m 이동 가능


# 맨하탄 거리 계산해서 도달가능 여부 반환
def is_ok(x1, y1, x2, y2):
    if abs(x1-x2) + abs(y1-y2) <= M:
        return True
    return False


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    # 시작 idx: 0 목적 idx :N+1
    points = [list(map(int, input().split())) for _ in range(N+2)]
    q = deque()
    visited = [0]*(N+2)
    ex, ey = points[N+1]

    # 시작지점(집) 추가
    q.append(0)
    visited[0] = 1
    # spos는 points에 넣지 않았으므로 visited는 pass

    happy = False
    while q:
        cx, cy = points[q.popleft()]
        if cx == ex and cy == ey:   # 도착 지점 도달하면 break
            happy = True
            break
        for i in range(N+2):
            nx, ny = points[i]
            if visited[i] == 0 and is_ok(cx, cy, nx, ny): # 방문한 적없고 1000m 내에 도달 가능하다면 방문처리하고 q에 삽입
                visited[i] = 1
                q.append(i)

    if happy:
        print("happy")
    else:
        print("sad")