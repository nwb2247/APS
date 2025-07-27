import heapq
hq = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(hq) != 0:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        # heapq의 경우 정렬 기준이 여러개일 때, tuple형태로 넣어주면 됨
        heapq.heappush(hq, (abs(num), num))