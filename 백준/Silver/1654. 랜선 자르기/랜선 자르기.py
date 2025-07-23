N, K = map(int, input().split())
lst = [0]*N
for i in range(N):
    lst[i] = int(input())

left = 0
right = 2**32-1

while left <= right:
    mid = (left+right)//2
    cnt = sum(map(lambda x: x//mid, lst))
    if cnt >= K:
        left = mid + 1
    else:
        right = mid - 1


print(right)
