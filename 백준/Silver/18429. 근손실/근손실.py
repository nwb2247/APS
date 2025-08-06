"""
각 운동키트 한번만 사용가능
500 이상 유지
중량 K만큼 감소
500 이상 유지되도록 하는 경우의 수 출력
"""

def dfs(depth, w): # depth 직전까지의 일수 (0일 1일,,)
    global ans

    if w < 500:
        return
    
    if depth == N and w >= 500:
        ans += 1

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(depth+1, w-K+lst[i])
            visited[i] = 0



N, K = map(int, input().split())
lst = list(map(int, input().split()))
visited = [0]*N
ans = 0
dfs(0, 500)
print(ans)
