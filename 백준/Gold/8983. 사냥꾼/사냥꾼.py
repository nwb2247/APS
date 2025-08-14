"""
잡을 수 있는 동물의 수
M*N 시간 초과
이분탐색 or 투포인터

이분탐색 :
각 동물별로 잡을 수 있는 사대가 있는지를 이분탐색으로 확인
잡을 수 있다면 count
(단, L넘으면 어떤 사대도 불가이므로 바로 넘김)


투포인터 :
동물의 위치에 따라 사대 인덱스를 늘릴지, 동물 인덱스를 늘릴지 결정
=> 이를 위해 사대를 x위치에 따라 정렬, 동물도 양 대각 축을 기준으로 정렬
animals.sort(key=lambda x: (x[0]+x[1], x[0]-x[1]))
(animals.sort(key=lambda x: (x[0]+x[1], x[1]-x[0]) 로 하면
아직 잡을 수 있는 동물이 있는데 사대를 움직여야하므로 틀림)
"""
M, N, L = map(int, input().split()) # M사대 N동물
sade = list(map(int, input().split()))
sade.sort()
animals = [tuple(map(int, input().split())) for _ in range(N)]
animals.sort(key=lambda x:x[0])

def check(ax, ay, m):
    return abs(ax-sade[m]) + ay <= L

cnt = 0
for ax, ay in animals:
    if ay > L:          # L보다 크면 가능한 사대 없으므로 바로 넘김 (시간 단축)
        continue
    l, r = 0, M-1
    while l<=r:
        m = (l + r)//2
        if check(ax, ay, m):        # 사대 사정거리 안에 있으면 cnt += 1해주고 다음 동물로 넘김
            cnt += 1
            break
        elif ax < sade[m]:
            r = m-1
        else:
            l = m+1
    # 결국 찾지 못하고 l>r되면 넘어감
print(cnt)


# # 투포인터
# animals.sort(key=lambda x: (x[0]+x[1], x[0]-x[1]))
# # print(animals)
#
# s = 0
# a = 0
#
# cnt = 0
# while s<M and a<N:
#     if (abs(sade[s]-animals[a][0]) + animals[a][1]) <= L:
#         # 잡을 수 있으면 잡고 다음 동물 확인
#         a += 1
#         cnt += 1
#     elif animals[a][1] > L or animals[a][0] < sade[s]:
#         # 동물의 y값이 L을 넘으면 사대를 옮겨도 못잡으므로 넘김
#         # animals[a][0] < sade[s]도 가능한 동물이 나올때까지 넘김
#         a += 1
#     else:
#         # animals[a][0] >= sade[s]면 현재 사대는 불가능하지만
#         # 가능한 사대가 있을 수 있으므로 사대를 넘김
#         s += 1
#
# print(cnt)
