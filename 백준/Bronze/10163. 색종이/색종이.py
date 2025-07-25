arr = [[-1]*1001 for _ in range(1001)]
N = int(input())
for i in range(N) :
    sc, sr, w, h = map(int, input().split())
    for r in range(sr, sr+h) :
        for c in range(sc, sc+w) :
            arr[r][c] = i
cnts = [0]*N
for r in range(1001) :
    for c in range(1001) :
        num = arr[r][c]
        if num != -1 :
            cnts[num] += 1
        # else :
        #     pass
print(*cnts, sep="\n")

