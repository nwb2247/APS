"""
[요약평]
문제를 잘 읽고 조건 분기 (ex) 한 좌표에 한 구름만 도착한 경우))

[타임라인]
(녹화 파일이 깨져 정확하지 않음)
이해 및 구상 10분
구현 15분
디버깅 5분
---------------
총 30분

[이해 및 구상]
-) 구름 도착을 일단은 narr로 받고, 시간초과 dict 사용해보기로 함
    => 미리 좀 더 고민해서 시간 복잡도를 생각해보았다면 좋았을듯
+) 0와 N-1이 연결되므로 oob가 필요없음을 생각하고 시작
+) 여러 정보를 클래스가 아닌 배열로 표현할때 각 위치의 정보를 종이에 한번더 적어둠
+) 구름 위치 -1씩 빼주기 확인

[구현]
+) 모두 홀수 or 짝수 를 어떻게 구할지 미리 생각못했지만, 구현 과정에서 잘 구상하여 구현함

[디버깅]

"""

from collections import deque

N, M, K = map(int, input().split())
q = deque()
# arr = [[[] for _ in range(N)] for _ in range(N)] (D) 외부에 arr을 표현할 이유가 없었음..

ds = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    q.append((r-1, c-1, m, s, d))

for _ in range(K):
    narr = [[[] for _ in range(N)] for _ in range(N)]
    while q:
        cr, cc, m, s, d = q.popleft()
        dr, dc = ds[d]
        nr = (cr+dr*s)%N
        nc = (cc+dc*s)%N
        narr[nr][nc].append((m, s, d))

    for cr in range(N):
        for cc in range(N):
            if len(narr[cr][cc]) == 1: # 하나인 경우는 그냥 추가
                cm, cs, cd = narr[cr][cc][0]
                q.append((cr, cc, cm, cs, cd))
                continue

            nm = sum(map(lambda x:x[0], narr[cr][cc])) // 5
            if nm == 0:
                continue
            ns = sum(map(lambda x:x[1], narr[cr][cc])) // len(narr[cr][cc])

            all_odd = True
            all_even = True
            for _, _, cd in narr[cr][cc]: # (D) narr에는 3가지 정보만 넣었음,,,
                if cd%2 == 0:
                    all_odd = False
                else:
                    all_even = False

            nd = [1, 3, 5, 7]
            if all_odd or all_even:
                nd = [0, 2, 4, 6]

            for i in nd:
                q.append((cr, cc, nm, ns, i))

    # for l in narr:
    #     print(l)
    #
    # print(q)

ans = 0
while q:
    info = q.popleft()
    ans += info[2]
print(ans)

