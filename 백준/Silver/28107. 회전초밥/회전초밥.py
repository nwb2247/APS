"""
손님 N<=100_000
초밥의 수 M<=200_000
모든 손님의 초밥 주문 수의 합 <= 200_000
초밥의 종류는 1~200001으로

메모리제한 1024mb

초밥하나씩 꺼내면서 누구줄지 매번 돌면서 결정하면 N*M 시간 초과

각 초밥 종류별로 우선순위큐 넣고, 손님 인덱스 돌면서 해당 초밥 원하면 넣어줌

초밥 하나씩 확인하면 맨앞 빼고 cnt 올려줌
"""
from heapq import heapify, heappop

N, M = map(int, input().split())    # N: 손님수, M: 초밥 수
forwhom = dict()                    # forwhom[s] : s를 누구에게 줄것인가?
cnt = [0]*N                         # cnt[i] i손님이 몇개 먹었는가
for i in range(N):
    k, *inp = map(int, input().split())
    for s in inp:
        if s not in forwhom:
            forwhom[s] = []
        forwhom[s].append(i)        # i손님이 s먹고 싶으면 forwhom[s]에 i append

for s in forwhom:
    heapify(forwhom[s])             # 앞손님이 먼저 먹게 해야하므로 heapify

sushi = list(map(int, input().split()))

for s in sushi:
    if s in forwhom and forwhom[s]:     # s가 forwhom에 있고 s를 먹고 싶어하는 사람이 아직 있다면, 
        cnt[heappop(forwhom[s])] += 1   # 종류 만날때 마다 하나씩 줌

print(*cnt)