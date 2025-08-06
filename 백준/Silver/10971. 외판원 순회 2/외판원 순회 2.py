"""
갈 수 없는 곳은 0으로 주어짐
"""


def dfs(depth, prev, sm):
    # depth: 지금까지 몇군데 들렸는지
    # prev : 직전에 어디였는지
    # 지금까지 비용
    global mn

    if sm > mn: # 가지치기 (이미 mn 넘었다면 볼 필요 X)
        return

    if depth == N:    # N군데 다들렸다면 -> 다시 처음으로 돌아가는 곳 넣어줌
        if arr[prev][si] != 0: # arr[prev][i]==0은 갈수 없는 곳이므로 패스
            mn = min(mn, sm+arr[prev][si])
        return

    for i in range(N):
        if visited[i] == 0 and arr[prev][i] != 0: # arr[prev][i]==0은 갈수 없는 곳이므로 패스
            visited[i] = 1
            dfs(depth+1, i, sm+arr[prev][i])
            visited[i] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N
ans = float('inf')
for si in range(N):
    mn = float('inf')
    visited[si] = 1
    dfs(1, si, 0)
    ans = min(ans, mn)
    visited[si] = 0
print(ans)
