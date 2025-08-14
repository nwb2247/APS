"""
일단 다 더하고, mst써서 최소길이합 구하고 빼줌
방향있는 그래프?
"""
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)


def to_int(c):
    if ord("a") <= ord(c) <= ord("z"):
        return ord(c)-ord("a")+1
    elif ord("A") <= ord(c) <= ord("Z"):
        return ord(c)-ord("A")+27
    elif c == "0":
        return 0

N = int(input())
arr = [list(map(lambda x:to_int(x), input())) for _ in range(N)]

parent = [i for i in range(N)]

adj = []
total = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            total += arr[i][j]
            adj.append((arr[i][j], i, j)) # 가중치, 다음 번호
adj.sort()
sm = 0
found = 0
for w, s, e in adj:
    if find(s) == find(e):
        continue
    found += 1
    sm += w
    union(s, e)

if found == N-1:
    print(total-sm)
else:
    print(-1)

