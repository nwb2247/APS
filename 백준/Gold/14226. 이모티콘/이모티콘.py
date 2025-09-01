"""
S만들기
한개가 화면에 있는 상태
1. 모두 복사
2. 모두 붙여 넣기
3. 화면 임티중 한개 삭제
"""
from collections import deque

S = int(input())
v = [[-1]*(2*S+1) for _ in range(2*S+1)]
# K[a][b] : a 화면상 개수 b 클립보드상 개수
v[1][0] = 0
q = deque()
q.append((1, 0))
while q:
    cs, ccb = q.popleft()

    if cs == S:
        print(v[cs][ccb])
        break

    if v[cs][cs] == -1:         # 클립보드에 복사 연산
        v[cs][cs] = v[cs][ccb] + 1
        q.append((cs, cs))

    if ccb != 0 and cs + ccb <= 2*S and v[cs + ccb][ccb] == -1:  # 불여넣기
        v[cs + ccb][ccb] = v[cs][ccb] + 1
        q.append((cs + ccb, ccb))

    if cs != 0 and v[cs-1][ccb] == -1:  # 화면에서 하나빼기
        v[cs-1][ccb] = v[cs][ccb] + 1
        q.append((cs-1, ccb))
