def bt(depth, perm, visited):

    if depth == M:          # 깊이가 M이 도달했으면 출력
        print(*perm)
        return

    for i in range(N):              # N을 돌면서
        if not visited[i]:          # 방문하지 않은 인덱스에 대해
            visited[i] = True       # 방문처리하고 perm에 추가하고
            perm[depth] = lst[i]    
            bt(depth+1, perm, visited)  # 다음 수열 찾기 위해 bt
            visited[i] = False          # 원상 복구

def solve():
    lst.sort()
    perm = [0] * M
    visited = [False] * N
    bt(0, perm, visited)


N, M = map(int, input().split())
lst = list(map(int, input().split()))
solve()

