"""
최소값과 최대값을 둘다 제거 가능

최소 큐, 최대 큐 사용해서
넣을 때는 둘다 넣어주고, 뺄때는 해당하는 곳에 빼면서
dict에 넣어 있는지 확인하고 빼주기
(K <= 1000000이므로 dict ok)

주의 : maxheap -붙이기
"""

import sys
from heapq import heappop, heappush
from collections import defaultdict

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    minheap = []
    maxheap = []
    dmin = defaultdict(int)
    dmax = defaultdict(int)

    for _ in range(K):
        cmd, numst = sys.stdin.readline().split()
        num = int(numst)
        
        # 연산
        if cmd == "I":
            heappush(minheap, num)
            heappush(maxheap, -num)
        else:   # D
            if num == -1 and minheap:
                dmax[-heappop(minheap)] += 1
            elif maxheap: # 1:
                dmin[-heappop(maxheap)] += 1

        # 연산이 끝나면 최소힙, 최대힙에 빼줘야할게 있는지 확인하기
        while minheap and dmin[minheap[0]] > 0:
            dmin[heappop(minheap)] -= 1
        while maxheap and dmax[maxheap[0]] > 0:
            dmax[heappop(maxheap)] -= 1

        # print(cmd, num)
        # print(dmin)
        # print(dmax)
        # print(minheap)
        # print(maxheap)
        # print()
        
    if not minheap: # minheap이 비었다면 maxheap도 당연하게 비어있음
        print("EMPTY")
    else:
        print(-maxheap[0], minheap[0]) # 주의 : maxheap엔 - 붙이기