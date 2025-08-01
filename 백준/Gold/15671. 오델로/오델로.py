N = int(input())
lst = [list(map(lambda x:int(x)-1, input().split())) for _ in range(N)]

ds = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

arr = [["."]*6 for _ in range(6)]
arr[2][2] = "W"
arr[3][3] = "W"
arr[2][3] = "B"
arr[3][2] = "B"

for i in range(N):
    sr, sc = lst[i]
    if i%2 == 0: # B
        arr[sr][sc] = 'B'
        no = False
        for dr, dc in ds:
            flip = True
            l = 1
            while True:
                if not (0<=sr+l*dr<6 and 0<=sc+l*dc<6):
                    flip = False
                    break
                elif arr[sr+l*dr][sc+l*dc] == '.':
                    flip = False
                    break
                elif arr[sr+l*dr][sc+l*dc] == 'W':
                    l += 1
                elif arr[sr+l*dr][sc+l*dc] == 'B':
                    l -= 1
                    break
            if not flip:
                continue
            for nl in range(1, l+1):
                arr[sr + nl * dr][sc + nl * dc] = "B"
    else: # W
        arr[sr][sc] = 'W'
        no = False
        for dr, dc in ds:
            flip = True
            l = 1
            while True:
                if not (0 <= sr + l * dr < 6 and 0 <= sc + l * dc < 6):
                    flip = False
                    break
                elif arr[sr + l * dr][sc + l * dc] == '.':
                    flip = False
                    break
                elif arr[sr + l * dr][sc + l * dc] == 'B':
                    l += 1
                elif arr[sr + l * dr][sc + l * dc] == 'W':
                    l -= 1
                    break
            if not flip:
                continue
            for nl in range(1, l + 1):
                arr[sr + nl * dr][sc + nl * dc] = "W"

for lst in arr:
    print(*lst, sep="")
w_cnt = 0
b_cnt = 0
for lst in arr:
    w_cnt += lst.count("W")
    b_cnt += lst.count("B")
if w_cnt>b_cnt:
    print("White")
else:
    print("Black")

