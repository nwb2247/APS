def bt(depth):
    if depth == M:
        st = " ".join(list(map(lambda x: str(x), selected)))
        if st not in st_set:
            st_set.add(st)
            print(st)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            selected[depth] = lst[i]
            bt(depth+1)
            visited[i] = False


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
st_set = set()
visited = [False]*N
selected = [0]*M
bt(0)

