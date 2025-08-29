from collections import defaultdict

er, ec, K = map(int, input().split())
er -= 1
ec -= 1
Z = 100
arr = [list(map(int, input().split())) for _ in range(3)]

def row_op(arr):

    for r in range(len(arr)):
        cnt = defaultdict(int)
        for c in range(len(arr[r])):
            if arr[r][c] != 0:
                cnt[arr[r][c]] += 1
        tmp = []
        for k, v in cnt.items():
            tmp.append((k, v)) # 수, 개수
        tmp.sort(key=lambda x: (x[1], x[0]))
        arr[r] = []
        for num, c in tmp:
            arr[r].append(num)
            arr[r].append(c)
        if len(arr[r]) > Z:
            arr[r] = arr[r][:Z]
    mxlen = max(map(len, arr))
    for r in range(len(arr)):
        for _ in range(mxlen - len(arr[r])):
            arr[r].append(0)

    return arr

t = 0
while True:
    # 되는지부터 확인
    if er<len(arr) and ec<len(arr[0]) and arr[er][ec] == K:
        break
    t += 1
    if t > 100:
        t = -1
        break
    if len(arr) >= len(arr[0]):
        arr = row_op(arr)
    else:
        arr_t = [list(lst) for lst in zip(*arr)]
        arr_t = row_op(arr_t)
        arr = [list(lst) for lst in zip(*arr_t)]

print(t)


