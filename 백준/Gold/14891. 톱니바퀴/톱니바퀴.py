from collections import deque

deqs = [deque() for _ in range(4)]

for i in range(4):
    lst = list(map(int, input().rstrip()))
    for num in lst:
        deqs[i].append(num)

K = int(input())
for _ in range(K):
    inp = input().split()
    i = int(inp[0]) - 1  # 인덱스 입력을 -1 해서 받아옴
    ds = [0]*4
    ds[i] = int(inp[1])  # 방향 1(시계방향) pop -> appendleft / -1(반시계방향) popleft -> append

    for j in range(i, 0, -1): # i부터 1까지
        if deqs[j][6] != deqs[j-1][2]:
            ds[j-1] = ds[j]*(-1)
        else:
            break

    for j in range(i, 4-1): # i부터 2까지
        if deqs[j][2] != deqs[j+1][6]:
            ds[j+1] = ds[j]*(-1)
        else:
            break

    for j in range(4):
        if ds[j] == 1:  # 시계방향이면
            deqs[j].appendleft(deqs[j].pop())
        elif ds[j] == -1:                       # else로빼면 안됨 (0인 경우에는 아무것도 하면 안되므로)
            deqs[j].append(deqs[j].popleft())

    # print(i, ds[i], ds)
    # for deq in deqs:
    #     print(deq)

ans = 0
for i, deq in enumerate(deqs):
    ans += 2 ** i * deq[0]

print(ans)
