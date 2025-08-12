"""
두 묶음씩 꺼내서 비교해주고, 하나의 큰 묶음으로 만들어서 다시 넣음

ex) 10 10 10 10 10를 순차적으로 한묶음씩만 비교하면 20 + 30 + 40 + 50 = 140번 비교

10 10 10 10 10
10 + 10 => 20

10 10 10 20
10 + 10 => 20

10 20 20
10 20 => 30

20 30 =>
50

20 + 20 + 30 + 50 = 120번 비교

"""

from heapq import heappop, heappush, heapify

N = int(input())
pq = [int(input()) for _ in range(N)]
heapify(pq) # (D) 처음에 heapify 안해줌;;;

cnt = 0
while len(pq) > 1:              # 하나가 남아있다 => 더 이상 비교 필요없다, 비교 끝났다.
    t = heappop(pq) + heappop(pq)   # 제일 작은 카드 뭉치 두개 꺼내서 더해줌
    cnt += t                        # 비교횟수에 추가
    heappush(pq, t)                 # 합친 카드 뭉치 다시 넣어줌

print(cnt)
