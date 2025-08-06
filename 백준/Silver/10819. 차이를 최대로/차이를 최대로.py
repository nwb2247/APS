N = int(input())

def dfs(depth):
    global ans

    if depth == N:
        sm = 0
        for i in range(N-1):
            sm += abs(order[i]-order[i+1])
        ans = max(ans, sm)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            order[depth] = lst[i]
            dfs(depth+1)
            visited[i] = 0


lst = list(map(int, input().split()))

order = [0]*N
ans = 0
visited = [0]*N
dfs(0)

print(ans)