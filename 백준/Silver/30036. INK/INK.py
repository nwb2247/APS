I, N, K = map(int, input().split())

ink = input()
arr = [list(input()) for _ in range(N)]
ops = list(input())

ds = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}

def oob(r, c):      # out of bound
    return not (0<=r<N and 0<=c<N)

def coloring():
    global  color_idx, color_size
    for nr in range(cr-color_size, cr+color_size+1):
        for nc in range(cc-color_size, cc+color_size+1): #(D) : +1을 안해줌;;;
            if abs(nr-cr) + abs(nc-cc) <= color_size:
                if not oob(nr, nc) and arr[nr][nc] not in ["@", "."]:
                    arr[nr][nc] = ink[color_idx]
    color_size = 0
    color_idx = (color_idx+1)%I

def move(op):
    global cr, cc
    dr, dc = ds[op]
    nr, nc = cr+dr, cc+dc
    if not oob(nr, nc) and arr[nr][nc] == ".":
        arr[cr][cc] = "."
        arr[nr][nc] = "@"
        cr, cc = nr, nc

f = False
for sr in range(N):
    for sc in range(N):
        if arr[sr][sc] == "@":
            f = True
            break
    if f:
        break

color_idx = 0
color_size = 0
cr, cc = sr, sc
for op in ops:
    if op == "j":
        color_size += 1
    elif op == "J":
        coloring()
    elif op in ds.keys():
        move(op)
    else:
        print("!!!!!")

for lst in arr:
    print("".join(lst))



