"""
잡을 수 있는 동물의 수

M*N 시간 초과

# 사로를 정렬
# 각 동물 들에 대해서 어느 사로 범위에서 잡힐 수 있는지 계산하고,
# 그 범위에 사로가 존재하는지 이분탐색
투포인터
"""


M, N, L = map(int, input().split()) # M사대 N동물
sade = list(map(int, input().split()))
sade.sort()
animals = [tuple(map(int, input().split())) for _ in range(N)]
animals.sort(key=lambda x: (x[0]+x[1], x[0]-x[1]))

# print(animals)

s = 0
a = 0

cnt = 0
while s<M and a<N:
    if (abs(sade[s]-animals[a][0]) + animals[a][1]) <= L:
        a += 1
        cnt += 1
    elif animals[a][1] > L or animals[a][0] < sade[s]:
        a += 1
    else:
        s += 1

print(cnt)