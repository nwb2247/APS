"""
그림 상으로 1번부터 2N
1-> 올리는 위치 (0번부터 시작한다면 0이 )
N 내리는 위치    (0번부터 시작한다면 N-1)

올리는 위치에만 올릴 수 있음
내리는 위치 도착하면 "즉시"!!! 내림

로봇 스스로 이동가능
올리거나 이동하면 그 칸(도착칸)은 항상 내구도가 1감소

1. 벨트가 한칸씩 회전
    (내리는 위치 확인)
2. 가장 먼저 올라간 로봇부터 이동할 수 있다면 이동, 할 수 없다면 가만히
    이동조건 : 이동하려는 칸에 로봇이 없거나, 내구도가 1이상 남아있어야함
    (이동해서 내리는 위치 도착하면 내림)
3. 올리는 칸의 내구도가 0이 아니라면 올려줌
4. 내구도가 0인 칸의 개수가 K개 "이상"!!!!!이라면 과정 종료
    그렇지 않으면 1로 돌아감

이 하나의 단계

종료시 몇 단계 진행중이었는가? (단, 처음 단계는 1번째 단계)

sec = 0으로 두고
while True:
    시작하자마자 1로 두기

올리는 위치, 내리는 위치를 회전 시켜주고
로봇는 lst로 관리하자. 단 가장 먼저 올라간 로봇은 lst[0]
즉 0부터 마지막 로봇까지 움직여줌

가장 오래된 로봇 =>

"""
from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))


up, down = 0, N-1 # 업데이트시 %2N
sec = 0
robots = []
robot_idx = 0
belts = [0]*2*N
cnt = 0
while True:
    sec += 1
    up = (up + 2*N-1)%(2*N)
    down = (down + 2*N-1)%(2*N)

    for i in range(len(robots)):
        if robots[i] == down:
            belts[down] = 0
            robots.pop(i)
            break

    for i in range(len(robots)):
        pos = robots[i]
        npos = (pos + 1)%(2*N)
        if belts[npos] == 0 and A[npos] > 0:
            robots[i] = npos
            A[npos] -= 1
            if A[npos] == 0:
                cnt += 1
            belts[npos] = 1
            belts[pos] = 0

    for i in range(len(robots)):
        if robots[i] == down:
            belts[down] = 0
            robots.pop(i)
            break

    if A[up] > 0:
        robots.append(up)
        belts[up] = 1
        A[up] -= 1
        if A[up] == 0:
            cnt += 1

    if cnt >= K:
        break

    # print("sec ",sec)
    # print("up", up, "down", down)
    # print("robots ", robots)
    # print("belts ", belts)
    # print("A ", A)
    # print()

print(sec)




