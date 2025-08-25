"""
[한줄평]
간단하게라도 손구상 꼭 하자
손구상이 주석구상 보다 빠르게 정리가능, 간단하게 손코딩으로 구조 잡기

[타임라인]
이해 및 구상 : 8분
구현 : 10분
디버깅 : 7분
-----
총 25분

[구상]
+) 손구상, 손코딩으로 구조 잡고 들어가기
+) day의 출력 방법 잡고 들어간 것 나쁘지 않은듯
+) L, R 조건 이상 이하 확실히 해둠
-) while 종료 조건을 좀만 더 확실하게 잡고 갔더라면..

[구현]
+) check 함수 good
-) lambda 사용법 잘 기억 안난다면 한번 시험해보거나 주석 처리해두면 좋을듯 (실수 방지)
-) 차분하게 주석도 적으면서 가기

[디버깅]
+) print, 디버거로 구상 부분에서 꼼꼼하지 못했던 종료조건 문제 캐치

[시간복잡도]
2000 * 50(N) * 50 ?

[엣지케이스]
(하루도 이동이 일어나지 않는 경우)
2 10 10
10 50
20 30
------
0

"""


# (손구상 요약)
# L<= <=R 주의
# 매 횟수 마다 visited 초기화
# BFS로 연합찾고
# pos에 담아주고 합 구해서 적용시켜줌
# cnt 이용해서 연합이 더 이상 만들어지지 않으면 while break
# 단 출력시 day-1를 출력 (마지막 날은 연합이 없어 이동이 이뤄지지 않은 날이므로)

from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

DS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def oob(r, c):
    return not (0 <= r < N and 0 <= c < N)


def check(cr, cc, nr, nc):      # 연합 결성 L, R 조건 확인
    return L <= abs(arr[cr][cc] - arr[nr][nc]) <= R


day = 0
while True:
    day += 1
    visited = [[0] * N for _ in range(N)]
    cnt = 0 # (1이면 break)
    for sr in range(N):
        for sc in range(N):
            if visited[sr][sc] == 0:
                q = deque()
                cnt += 1
                pos = []

                visited[sr][sc] = 1
                q.append((sr, sc))
                pos.append((sr, sc)) # (D) pos에도 넣어줘야함
                
                while q:
                    cr, cc = q.popleft()

                    for dr, dc in DS:
                        nr, nc = cr+dr, cc+dc
                        if oob(nr, nc):
                            continue
                        if visited[nr][nc] == 0 and check(cr, cc, nr, nc):
                            visited[nr][nc] = 1
                            pos.append((nr, nc))
                            q.append((nr, nc))

                sm = sum(map(lambda p:arr[p[0]][p[1]], pos)) # (D) : lambda는 자동 언패킹 안됨
                for r, c in pos:
                    arr[r][c] = sm//(len(pos))

    if cnt == N*N: # (D) 더 이상 두 국가가 연합을 이루지 않는 경우로 해야함 (처음에는 잘못생각해서 1로 둠;;;)
        break

print(day-1)



