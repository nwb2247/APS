"""
1, 1 가 맨위 좌측
사과 위치 받을때 -1씩 빼주기

벽이나 자기 자신과 부딪히면 게임 끝 -> 맵에다가 뱀을 표현, oob도 구현
0, 빈공간
1, 사과
2, 뱀
뱀의 좌표는 queue를 이용하자, 꼬리 없어지면 맵에도 갱신해주기

처음에는 오른쪽을 향함
!!! (D) 방향 전환
X가 "끝난뒤" 방향 전환, 즉 3에 방향전환이라면, 진행 먼저하고 맨마지막에 방향전환

몇초에 끝나는지 출력, 0으로 시작하고 while 시작하면서 1초 늘려주기
해당 초가 되면 명령어 수행하는 것이므로, 명령어도 queue로 관리

"""
from collections import deque

to_int = {"D":1, "L":-1}
ds = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우하좌상 (D 기준)

N = int(input()) # 보드의 크기 <= 100
K = int(input()) # 사과의 개수 <= 100
arr = [[0]*N for i in range(N)]

for i in range(K):
    ar, ac = map(int, input().split())
    arr[ar-1][ac-1] = 1

L = int(input()) # <= 100
coms = deque()
for i in range(L):
    st = input().split()
    coms.append((int(st[0]), to_int[st[1]]))

def oob(r, c):
    return not (0<=r<N and 0<=c<N)

pos = deque()
pos.append((0, 0)) # r, c
arr[0][0] = 2
# for l in arr:
#     print(l)

cd = 0
sec = 0
while True:
    sec += 1

    cr, cc = pos[-1]
    dr, dc = ds[cd]
    nr, nc = cr+dr, cc+dc
    if oob(nr, nc) or arr[nr][nc] == 2:
        break
    elif arr[nr][nc] != 1: # 사과가 없으면
        tail_r, tail_c = pos.popleft()
        arr[tail_r][tail_c] = 0

    pos.append((nr, nc))
    arr[nr][nc] = 2

    if coms and coms[0][0] == sec:
        cd = (cd + coms.popleft()[1])%4 # 오른쪽이면 += 1 왼쪽이면 -= 1

    # print(sec)
    # for l in arr:
    #     print(l)
    # print()

print(sec)

