import heapq, sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    min_q = []
    min_history = dict()
    max_q = []
    max_history = dict()

    N = int(input())
    for _ in range(N):
        st = input().split()
        # print(st)
        op = st[0]
        num = int(st[1])
        if op == "I":
            heapq.heappush(min_q, num)
            heapq.heappush(max_q, -num)
        else:
            if num == -1:
                # get(a, b) : 있으면 dict[a]를 반환, 없으면 b를 반환
                # 즉 값이 있는데 0이거나 값이 없어서 0을 반환한다면...
                while len(min_q) > 0 and max_history.get(min_q[0], 0) != 0:
                    pop_val = heapq.heappop(min_q)
                    max_history.update({pop_val: max_history.get(pop_val) - 1})
                if len(min_q) > 0:
                    pop_val = heapq.heappop(min_q)
                    min_history.update({pop_val: min_history.get(pop_val, 0) + 1})
            else:
                while len(max_q) > 0 and min_history.get(-max_q[0], 0) != 0:
                    pop_val = -heapq.heappop(max_q)
                    min_history.update({pop_val: min_history.get(pop_val) - 1})
                if len(max_q) > 0:
                    pop_val = -heapq.heappop(max_q)
                    max_history.update({pop_val: max_history.get(pop_val, 0) + 1})
        while len(min_q) > 0 and max_history.get(min_q[0], 0) != 0:
            pop_val = heapq.heappop(min_q)
            max_history.update({pop_val: max_history.get(pop_val) - 1})
        while len(max_q) > 0 and min_history.get(-max_q[0], 0) != 0:
            pop_val = -heapq.heappop(max_q)
            min_history.update({pop_val: min_history.get(pop_val) - 1})
        # print(max_q, min_q, max_history, min_history)
    if len(min_q) - sum(max_history.values()) == 0 and len(max_q) - sum(min_history.values()) == 0:
        print("EMPTY")
    else:
        print(-max_q[0], min_q[0])