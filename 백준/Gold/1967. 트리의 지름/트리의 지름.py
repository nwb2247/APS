"""
[조건]
노드 수 N 최대 10000
루트 노드와 자식 노드 관계 순차적으로 주어짐

[목표]
최대 지름 길이 구하기

[접근]
BFS 등 O(N^2) 알고리즘 시간 초과
대신 재귀를 이용해 각 간선을 타고 올라오면서 최대값을 갱신해주자
부모, 자식 default dict로 관리


[주의사항]
=> 이진 트리가 아닐 수 있다.
예제처럼 이진 트리 가능성만을 생각해서 두 경로의 합만을 생각해서 틀림
=> 두쌍의자식 경로 길이도 비교하여 ans에 반영

"""
from collections import defaultdict
import sys

sys.setrecursionlimit(20000)

def recur(cur):

    global ans

    if len(children[cur]) == 0:
        ans = max(ans, parent[cur][1])
        return parent[cur][1]

    mx = 0
    wlst = []
    for c in children[cur]:
        w = recur(c)
        mx = max(mx, w)
        wlst.append(w)

    for i in range(len(wlst)-1):
        for j in range(i+1, len(wlst)):
            ans = max(ans, wlst[i]+wlst[j])
    ans = max(ans, parent[cur][1] + mx)

    return parent[cur][1] + mx


N = int(input())
parent = defaultdict(tuple)    # 부모 노드와 거리를 같이 저장
children = defaultdict(list)      # 부모 노드 번호만 저장

for _ in range(N-1):
    p, c, w = map(int, input().split())
    children[p].append(c)
    parent[c] = (p, w)

parent[1] = (0, 0)

ans = 0

recur(1)

print(ans)
