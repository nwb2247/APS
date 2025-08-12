"""
N <= 100_000
PQ 시간 <= 1_000_000
비어있는 자리중 가장 작은 자리에 앉기

최대 1_000_000이므로 1초씩 늘려가며 진행
시작시간 순으로 정렬된 리스트에서 해당 초되면 pq에 넣어줌
컴퓨터 부족할 시에는 하나더 추가해서 넣어줌
이때 pq에는 종료시간과 시용중이었던 컴퓨터번호를 넣음 (종료시간 기준)
사람 수 N명이므로 컴퓨터 번호는 N개 넘어가지 않으므로 N개짜리 리스트로 컴퓨터 사용 cnt 관리

"""
from heapq import heappop, heappush
from collections import deque

N = int(input())
com_num = -1    # 첫컴퓨터 0번부터시작, 답출력시 1더해줌
coms = []       # 다음 사용가능 컴퓨터에 대한 pq
ongoing = []    # 사용중인 사람들 pq # 종료시간, 사용중 번호를 넣음
cnt = []        # 컴퓨터 사용 횟수

lst = [tuple(map(int, input().split())) for _ in range(N)]
lst.sort()
q = deque(lst)
start = q[0][0]
end = 0
for sh, eh in q:
    end = max(end, eh)


for ch in range(start, end+1):

    # 종료된 사람들부터 빼줌
    while ongoing and ongoing[0][0] == ch:
        _, com_to_stop = heappop(ongoing)
        heappush(coms, com_to_stop)

    while q and q[0][0] == ch:
        if len(coms) == 0:
            com_num += 1
            cnt.append(0)
            heappush(coms, com_num)
        com_to_use = heappop(coms)
        cnt[com_to_use] += 1
        heappush(ongoing, (q.popleft()[1], com_to_use))

print(com_num+1)
print(*cnt)
