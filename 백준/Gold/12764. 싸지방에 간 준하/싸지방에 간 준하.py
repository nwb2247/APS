"""
N <= 100_000
PQ 시간 <= 1_000_000
비어있는 자리중 가장 작은 자리에 앉기

최대 1_000_000이므로 1시간씩 늘려가며 진행
시작시간 순으로 정렬된 리스트에서 시작 시간되면 pq에 넣어줌
이때 pq에는 종료시간과 시용중이었던 컴퓨터번호를 넣음 (종료시간 기준)
컴퓨터 부족할 시에는 하나더 추가해서 넣어줌
컴퓨터 사용 cnt 관리

"""
from heapq import heappop, heappush
from collections import deque

N = int(input())
com_num = -1    # 첫컴퓨터 0번부터 시작, 따라서 총 필요한 컴퓨터는 com_num + 1
coms = []       # 다음 사람을 위해 사용 가능한 컴퓨터 번호에 대한 pq (노는 앞번호 컴퓨터부터 쓰므로)
ongoing = []    # 사용중인 사람, 컴퓨터에 대한 정보 pq # (종료시간, 사용중 번호), 종료시간 기준으로 들어감
cnt = []        # 각 컴퓨터 별 사용 횟수

lst = [tuple(map(int, input().split())) for _ in range(N)]  # (시작시간, 종료시간)
lst.sort()              # 시작시간 순으로 정렬
q = deque(lst)          # deque로 만들어줌 (시작 컴퓨터 인덱스 관리 복잡하므로,,,)

start = q[0][0]         # 가장빠른 시작 시간
end = 0                 # 가장느린 종료 시간
for sh, eh in q:
    end = max(end, eh)

for ch in range(start, end+1):                  # 시작부터 종료까지 시간 1단위씩 늘려가면서 진행

    # 시작보다 종료를 먼저 처리 (그래야 유휴 컴퓨터 관리 가능)
    while ongoing and ongoing[0][0] == ch:      # 지금 시간에 종료해야하는 사람들 다 빼줌
        _, com_to_stop = heappop(ongoing)       # 썼던 컴퓨터 번호 반납하고 다시 coms에 넣어줌
        heappush(coms, com_to_stop)

    while q and q[0][0] == ch:                  # 지금 시간에 시작해야하는 사람들 다 빼줌
        if len(coms) == 0:                      # 유휴 컴퓨터가 없다면 => 새 컴퓨터가 하나 더 필요함
            com_num += 1                        # 컴퓨터 인덱스 하나 늘리고 coms에 넣어줌
            cnt.append(0)
            heappush(coms, com_num)
        com_to_use = heappop(coms)              # 사용해야하는 컴퓨터 번호를 꺼냄
        cnt[com_to_use] += 1                    # 사용횟수 += 1
        heappush(ongoing, (q.popleft()[1], com_to_use))     # ongoing에 (종료시간, 컴퓨터 번호)를 넣어줌

print(com_num+1)      # 총사용해야하는 컴퓨터 수 (0번부터 시작하는 컴퓨터 인덱스에 1을 더해줌)
print(*cnt)           # 각 컴퓨터별 사용수
