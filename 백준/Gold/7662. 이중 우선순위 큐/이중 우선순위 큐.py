"""
d = dict()
...
d.get(a, default=b)
d에 key=a가 없는 경우, 원래는 None을 반환
그러나 default 파라미터를 명시하면 해당 값을 반환
"""

import heapq, sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):

    # 최소힙
    min_q = []
    # 최소힙에서 지워졌지만 최대힙에 반영되지 않은 것들
    min_history = dict()

    # 최대힙
    max_q = []
    # 최대힙에서 지워졌지만 최대힙에 반영되지 않은 것들
    max_history = dict()

    N = int(input())
    for _ in range(N):
        st = input().split()
        # print(st)
        op = st[0]
        num = int(st[1])
        # 삽입 연산인 경우 최대힙 최소힙에 모두 넣어줌
        if op == "I":
            heapq.heappush(min_q, num)
            heapq.heappush(max_q, -num)
        else:
            if num == -1:
                # 최소힙이 비어있지 않고, 최소힙 peek에 있는 값이 최대힙에서 지웠었지만 최소힙엔 아직 반영되지 않은 것이라면...
                    # get(a, b) : 있으면 dict[a]를 반환, 없으면 b를 반환
                    # 즉 값이 있는데 0이거나 값이 없어서 0을 반환한다면...
                while len(min_q) > 0 and max_history.get(min_q[0], 0) != 0:
                    pop_val = heapq.heappop(min_q)
                    new_cnt = max_history.get(pop_val) - 1
                    max_history.update({pop_val: new_cnt})
                # 위의 while문의 돌렸기 때문에 이제 진짜 최소값을 pop할 수 있다.
                if len(min_q) > 0:
                    pop_val = heapq.heappop(min_q)
                    # 최소힙에서 pop했지만 이는 나중에 최대힙에도 반영해야 하므로 min_history에 기록해둔다.
                    new_cnt = min_history.get(pop_val, 0) + 1
                    min_history.update({pop_val: new_cnt})
            else:
                while len(max_q) > 0 and min_history.get(-max_q[0], 0) != 0:
                    pop_val = -heapq.heappop(max_q)
                    new_cnt = min_history.get(pop_val) - 1
                    min_history.update({pop_val: new_cnt})
                if len(max_q) > 0:
                    pop_val = -heapq.heappop(max_q)
                    new_cnt = max_history.get(pop_val, 0) + 1
                    max_history.update({pop_val: new_cnt})
    # EMPTY여부, 최소 최대 값을 pop하기에 앞서 반영되지 않은 기록이 남아있다면 처리해준다.
    while len(min_q) > 0 and max_history.get(min_q[0], 0) != 0:
        pop_val = heapq.heappop(min_q)
        new_cnt = max_history.get(pop_val) - 1
        max_history.update({pop_val: new_cnt})
    while len(max_q) > 0 and min_history.get(-max_q[0], 0) != 0:
        pop_val = -heapq.heappop(max_q)
        new_cnt = min_history.get(pop_val) - 1
        min_history.update({pop_val: new_cnt})
        # print(max_q, min_q, max_history, min_history)
    if len(min_q) - sum(max_history.values()) == 0 and len(max_q) - sum(min_history.values()) == 0:
        print("EMPTY")
    else:
        print(-max_q[0], min_q[0])
