"""
(하부재귀 호출전 가지치기 연습)

항상 정답이 존재하는 경우만 주어짐
백트래킹
사전 순으로 가장 앞서는 방법만 출력, 즉 처음 발견하면 모두 종료
"""

# ---------------- 전처리 -----------------

ARR = [list(input()) for _ in range(5)]  # 그림

idxs = [(0, 4),  # 그림에서 빈칸 또는 숫자의 위치
        (1, 1), (1, 3), (1, 5), (1, 7),
        (2, 2), (2, 6),
        (3, 1), (3, 3), (3, 5), (3, 7),
        (4, 4)]

lst = [0] * 12  # idxs에 대응되는 숫자들
empty = []  # 비어있는 인덱스들 (백트래킹으로 채울예정)
use = [0] * 13  # 1~12중 사용된 숫자들 (no_use만들기 위한 중간과정)
for i, (r, c) in enumerate(idxs):
    if ARR[r][c] == "x":
        lst[i] = 0
        empty.append(i)
    else:
        lst[i] = ord(ARR[r][c]) - ord("A") + 1
        use[lst[i]] = 1

L = len(empty)
no_use = []  # 1~12중 사용되지 않은 숫자들 (empty와 리스트 크기 동일)
for i in range(1, 13):  # 자동으로 정렬됨. (사전 순으로 가장 앞서는 것 출력 가능)
    if use[i] == 0:
        no_use.append(i)

groups = [[0, 2, 5, 7],  # 합쳐져서 26이 되어야하는 lst의 인덱스 그룹
          [1, 2, 3, 4],
          [1, 5, 8, 11],
          [4, 6, 9, 11],
          [7, 8, 9, 10],
          [0, 3, 6, 10]]

where = [[] for _ in range(12)]  # lst의 각 인덱스에 대해 어느 그룹들에 속하는지
for i in range(12):
    for j, g in enumerate(groups):
        if i in g:
            where[i].append(j)

# ---------------- 백트래킹 -----------------


ans = []
found = False  # 답을 구했는지 아닌지 (구했으면 백트래킹 더이상 진행안함)
visited = [0] * L  # no_use[i]를 썼는지 안썼는지


def promising(depth):  # 하부 재귀 호출 전에 promising한지 확인하는 함수 (True면 호출)
    for w in where[empty[depth]]:  # 방금 채운 비어있던 인덱스가 족한 그룹에 대해
        g = groups[w]
        sm = 0
        for i in g:
            if lst[i] == 0:  # 아직 0인 것이 있으면 더 진행해볼만 하므로 건너뜀
                return True
            sm += lst[i]
        if sm != 26:  # 이미 한 그룹이 채워졌는데도, 합이 26과 다르다면 더 볼것도 없이 잘못됨 -> False 반환하고 가지치기
            return False
    return True  # 그 외 경우 (where[empty[depth]]의 그룹이 다 완성된 경우)는 promising하므로 진행


def check():        # 정답이 되는지 확인하기 위한 함수
    global found, ans
    if found:
        return

    for g in groups:        # 모든 그룹에 대해 26 되는지 확인
        sm = 0
        for i in g:
            sm += lst[i]
        if sm != 26:
            return

    found = True
    ans = lst[:]        # (사실 그냥 lst 써도 될듯)


def backtrack(depth):
    global found

    if depth == L:      # 모든 빈 인덱스 채웠으면 모두 26인지 확인
        check()
        return

    for i in range(L):
        if visited[i] == 0:
            visited[i] = 1              # 일단 방문처리 및 lst를 채워줌
            lst[empty[depth]] = no_use[i]
            
            if promising(depth):        # promising한지 확인
                backtrack(depth + 1)    # 맞다면 하부재귀 호출
            else:                       # 아니라면 반환하고 원상복구 
                visited[i] = 0
                lst[empty[depth]] = 0   # check(), promising() 등 위해서 lst도 원상복구 해야함
                continue                # 원복 후 다음거 진행  
                
            if found:                   # 하부 재귀의 위해 찾았으면 바로 함수 종료 (하나만 찾으면 되므로)
                return
            
            visited[i] = 0              # 하부 재귀 실행 종료 원복
            lst[empty[depth]] = 0


# ---------------- 실제 호출 -----------------
backtrack(0)

# ---------------- 출력 -----------------
for i, (r, c) in enumerate(idxs):
    ARR[r][c] = chr(ans[i] + ord("A") - 1)
for l in ARR:
    print("".join(l))
