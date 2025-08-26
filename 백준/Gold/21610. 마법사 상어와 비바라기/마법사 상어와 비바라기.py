"""
[한줄평]
그림 설명으로 이해 맞는지 확인
1, 1(좌표)또는 1(방향)으로 주어졌을 때 -1할 경우 문제가 발생할 부분이 있는지 확인하기
DS, OOB 등은 흐름 끊기지 않게 미리 만들자 (필요여부는 구상 단계에서 확인)
!!!자주하는 실수 : s만큼 이동해야하는데 자꾸 안곱해줌

[타임라인]
이해 및 구상 : 11분
구현 : 22분
디버깅 : 3분
---------
36분


[이해 및 구상]
-) 대각선 물복사버그 이해 잘못함 (그림으로 바로잡음)
-) 방향 손으로 그리고 인덱스 정리한것까지는 좋았으나, -1 할거면 -1된걸로 적어야 안헷갈릴듯
-) clouds를 deque로 구현하는 것 아닌지 헷갈렸음 (구상 단계 미흡 문제)
+) -1로 받아도 문제 발생하는지 안하는지 확인하기

[구현]
-) oob, ds, 맨하탄 거리 등 간단한 로직은 흐름 끊기지 않도록 미리 만들어두자
-) plus 배열 채우는 방법에 대해 미리 생각해보면 좋았을 듯 (append vs clouds와 같은 인덱스로 넣을지 )
+) 벽 넘어가 이동하는 로직 확인위해 print 간단히 찍어본 것
+) 함수화
+) 바구니 물 채우는 로직, 대각복사 로직 한번에 묶은 것
+) 대각 물복사에 의한 물채움을 바로 더해주지 않고 기록해뒀다가 한 것 좋았음
    (이 문제에선 괜찮지만, 경우에 따라 미리 더해서 문제가 되는 경우도 있음....)

[디버깅]
-) 엣지 등도 생각해보고 제출했을면 좋았을듯
+) 함수화로 오류 빠르게 잡음
+) clouds 를 리스트로 담아놔서 시간도 빨랐고 보기에도 좋았음
"""

# 방향 -1 씩

def oob(r, c):
    return not (0<=r<N and 0<=c<N)


def move(d, s):
    dr, dc = DS[d]
    for i in range(len(clouds)):
        cr, cc = clouds[i]
        nr, nc = (cr+dr*s)%N, (cc+dc*s)%N # (D) : s안곱해줌
        clouds[i] = (nr, nc)

def rain():
    for cr, cc in clouds:
        arr[cr][cc] += 1

    plus = [0]*len(clouds)
    for i in range(len(clouds)):
        cr, cc = clouds[i]
        for j in [1, 3, 5, 7]:
            dr, dc = DS[j]
            nr, nc = cr+dr, cc+dc
            if not oob(nr, nc) and arr[nr][nc]>0:
                plus[i] += 1

    for i in range(len(clouds)):
        cr, cc = clouds[i]
        arr[cr][cc] += plus[i]

def generate():
    new_clouds = []
    is_old = [[0]*N for _ in range(N)]
    for cr, cc in clouds:
        is_old[cr][cc] = 1
    for cr in range(N):
        for cc in range(N):
            if is_old[cr][cc] == 0 and arr[cr][cc] >= 2:
                new_clouds.append((cr, cc))
                arr[cr][cc] -= 2
    return new_clouds

DS = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
ops = []
for _ in range(M):
    d1, s = map(int, input().split())
    ops.append((d1 - 1, s))

clouds = [(N - 2, 0), (N - 2, 1), (N - 1, 0), (N - 1, 1)]

for d, s in ops:
    move(d, s)
    # print(clouds)
    rain()
    clouds = generate()

    # for l in arr:
    #     print(l)
    # print()

print(sum(map(sum, arr)))
