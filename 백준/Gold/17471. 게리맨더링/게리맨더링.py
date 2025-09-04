"""
[이해]
1~N개의 구역
두개의 선거구로 나눠야함
모두 두개 중하나에 포함
각 구역은 적어도 하나를 포함
각 구역은 모두 연결되어 있어야함

중간에 통하는 인접한 구역이 0개 이상? -> A에서 B로 갈 때 인접한 구역이 0개 이상어야함 (그 인접한 구역들은 모두 같은 선거구)
0개는 자기 자신?

인구차이를 최소화하는 방법 출력
2개로 나눌 수 없다면 -1 출력

[구상]

1번부터 로 bfs 돌려서 인접한 정점 덩어리가 몇개인지 찾기

3개 이상이면 -1
2개면 각각의 인구합 차 구하고 출력
1개면 (즉 모든 정점들이 연결되어있다면)
-> 백트래킹 (부분 집합, 2^10승 , 가능)

X개 고르고  X개의 정점으로만 이동하면서 갈 수 있는지 확인


"""
from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]
pop = [-1] + list(map(int, input().split()))
for ti in range(1, N + 1):
    _, *adjlst = map(int, input().split())
    adj[ti] = adjlst

# ----- 전처리 -----
def make_graph():
    v = [0]*(N+1)
    res = []
    for start in range(1, N+1):
        if v[start] == 1:
            continue

        tmp = []
        v[start] = 1
        q = deque()
        q.append(start)

        while q:
            cur = q.popleft()
            tmp.append(cur)

            for nxt in adj[cur]:
                if v[nxt] == 1:
                    continue
                v[nxt] = 1
                q.append(nxt)
        res.append(tmp)
    return res


def check(sset, start):
    v = [0]*(N+1)
    q = deque()
    v[start] = 1
    q.append(start)
    pos = []
    while q:
        cur = q.popleft()
        pos.append(cur)

        for nxt in adj[cur]:
            if nxt not in sset:
                continue
            if v[nxt] == 1:
                continue
            v[nxt] = 1
            q.append(nxt)
    return pos

def diff(g1, g2):
    sm1 = sum(map(lambda x: pop[x], g1))
    sm2 = sum(map(lambda x: pop[x], g2))
    return abs(sm1 - sm2)


def backtrack(depth, lst):
    global ans

    if depth == N+1:
        if len(lst) == 0 or len(lst) == N: # 양쪽에 하나씩은 있어야함..
            return
        lstset = set(lst)

        oppo = []
        for i in range(1, N+1):
            if i not in lstset:
                oppo.append(i)
        # 연결성 확인
        lst_conn = check(lstset, lst[0])        # lst
        oppo_conn = check(set(oppo), oppo[0])   # oppo
        if len(lst_conn) == len(lst) and len(oppo_conn) == len(oppo):
            # print(diff(lst, oppo))
            ans = min(ans, diff(lst, oppo))
        return

    backtrack(depth+1, lst + [depth])
    backtrack(depth+1, lst)



graphs = make_graph()
# print(graphs)

ans = float("inf")

if len(graphs) >= 3:
    ans = -1
elif len(graphs) == 2:
    ans = diff(graphs[0], graphs[1])
elif len(graphs) == 1: # 한개 라면...
    v = [0]*(N+1)
    backtrack(1, [])
# else: # 3개 이상이면 아무것도 안함
print(ans)

