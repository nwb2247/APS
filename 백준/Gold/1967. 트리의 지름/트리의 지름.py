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
=> 가장 길이가 긴 두 자식 경로 더해줌

1번쨰 2번째로 큰 수 구할 떼 조심할 점
mx1 = 0
mx2 = 0
for c in children[cur]:
    w = recur(c)
    if w >= mx1:
        mx2 = mx1
        mx1 = w
===> 이 방법 불가 ex 10, 0, 0, 5 이렇게 들어오면 두번째로 큰 값은 계속 0으로 남음

mx1 = 0
mx2 = 0
for c in children[cur]:
    w = recur(c)
    if w > mx1:
        mx2 = mx1
        mx1 = w
    elif w > mx2:
        mx2 = w
===> 이 방식이 올바른 방법
"""


"""
꿀팁 : 전역 변수는 한글자보다는 다소 번거롭게 지어야, 함수 내부에서 엉뚱하게 가져오는 실수를 줄일 수 있다.
"""

from collections import defaultdict
import sys

input = sys.stdin.readline

sys.setrecursionlimit(20000)

def recur(cur):

    global ans

    if len(children[cur]) == 0:
        # 자식이 없으면 부모와의 거리를 반환
        # (이를 위해 1의 부모를 0, 거리0의 dummy 노드 추가)
        ans = max(ans, parent[cur][1])
        return parent[cur][1]

    mx1 = 0 # 첫번째로 큰값
    mx2 = 0 # 두번째로 큰값
    for c in children[cur]: # 자식들에 대해
        w = recur(c)        # 재귀호출
        if w > mx1:         # 거리 w가 첫번째보다도 크면 한칸씩 밀어냄
            mx2 = mx1
            mx1 = w
        elif w > mx2:       # 첫번째와 같거나 작지만 두번째보단 크면 mx2에 저장
            mx2 = w

    ans = max(ans, mx1+mx2)
    ans = max(ans, parent[cur][1] + mx1)

    return parent[cur][1] + mx1


N = int(input())
parent = defaultdict(tuple)    # 부모 노드와 거리를 같이 저장
children = defaultdict(list)      # 부모 노드 번호만 저장
"""
defaultdict : 기본값을 지정, 인덱싱방식으로 없는 키의 값을 가져오려하면 빈리스트를 생성해줌
"""

# 꿀팁 : 전역 변수는 한글자보다는 다소 번거롭게 지어야, 함수 내부에서 엉뚱하게 가져오는 실수를 줄일 수 있다.
for _ in range(N-1):
    pp, cc, ww = map(int, input().split())
    children[pp].append(cc)           # 자식 번호만 추가
    parent[cc] = (pp, ww)              # 부모와 부모와의 거리도 추가

parent[1] = (0, 0)                  # 1의 부모처리를 통일성있게 하기 위해 0을 추가
ans = 0                             # 전역함수

recur(1)

print(ans)
