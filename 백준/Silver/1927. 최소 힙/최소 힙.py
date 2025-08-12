from heapq import heappop, heappush, heapify

N = int(input())
ops = [int(input()) for _ in range(N)]

pq = []
for op in ops:
    if op == 0:
        if pq:
            print(heappop(pq))  # 비어있지 않으면 heappop
        else:
            print(0)            # 비어있으면 0 출력
    else:
        heappush(pq, op)

