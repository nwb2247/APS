"""
항상 정답이 존재하는 경우만 주어짐
백트래킹
사전 순으로 가장 앞서는 방법만 출력, 즉 처음 발견하면 모두 종료
가지치기
"""

ARR = [list(input()) for _ in range(5)]
idxs = [(0, 4),
        (1, 1), (1, 3), (1, 5), (1, 7),
        (2, 2), (2, 6),
        (3, 1), (3, 3), (3, 5), (3, 7),
        (4, 4)]

lst = [0]*12
for i, (r, c) in enumerate(idxs):
    if ARR[r][c] == "x":
        lst[i] = 0
    else:
        lst[i] = ord(ARR[r][c]) - ord("A") + 1

empty = []
use = [0]*13
for i in range(12):
    if lst[i] == 0:
        empty.append(i)
    else:
        use[lst[i]] = 1
no_use = []
for i in range(1, 13):  # 자동으로 정렬됨.
    if use[i] == 0:
        no_use.append(i)

# print(empty, no_use)

groups = [[0, 2, 5, 7],
          [1, 2, 3, 4],
          [1, 5, 8, 11],
          [4, 6, 9, 11],
          [7, 8, 9, 10],
          [0, 3, 6, 10]]

where = [[] for _ in range(12)]
for i in range(12):
    for j, g in enumerate(groups):
        if i in g:
            where[i].append(j)

L = len(empty)
ans = [0]*L
found = False
visited = [0]*L # no_use[i]를 썼는지 안썼는지
final = []

def check():
    global found, final
    if found:
        False

    tmp = lst[:]
    for i in range(L):
        tmp[empty[i]] = ans[i]
    for g in groups:
        sm = 0
        for i in g:
            sm += tmp[i]
        if sm != 26:
            return False
    final = tmp
    found = True
    return True

def backtrack(depth):
    global ans, found

    if found:
        return

    if depth == L:
        check()
        return

    for i in range(L):
        if visited[i] == 0:
            visited[i] = 1
            ans[depth] = no_use[i]
            backtrack(depth + 1)
            visited[i] = 0

backtrack(0)
output = [chr(num + ord("A") - 1) for num in final]
for i, (r, c) in enumerate(idxs):
    ARR[r][c] = output[i]
for l in ARR:
    print("".join(l))



