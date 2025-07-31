from collections import deque

ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def rgb():
    cnt = 0         # 영역 수
    visited = [[0] * N for _ in range(N)]   
    for sr in range(N):     # 시작 지점 확인
        for sc in range(N):
            if visited[sr][sc] == 0:    # 방문하지 않은 경우
                cnt += 1                # cnt 추가하고 큐 생성, 시작점 큐에 삽입, 방문처리
                q = deque()

                visited[sr][sc] = 1
                q.append([sr, sc])

                while q:
                    cr, cc = q.popleft()
                    for dr, dc in ds:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:    # 범위 내 있고, 방문한 적 없고
                            if arr[nr][nc] == arr[sr][sc]:  # 시작점과 같은 색이라면
                                visited[nr][nc] = 1
                                q.append([nr, nc])
    return cnt


N = int(input())
ans = []
arr = [list(input()) for _ in range(N)]
ans.append(rgb())   # 색약이 아닌 사람의 영역 수 추가
for r in range(N):
    for c in range(N):
        if arr[r][c] == "R":        # 적색이라면 녹색으로 바꿔줌
            arr[r][c] = "G"
ans.append(rgb())   # 다시 영역 수 세고 정답 추가
print(*ans)
