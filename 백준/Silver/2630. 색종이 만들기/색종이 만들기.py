white = 0
blue = 0

def recur(sx, sy, size) :

    global white, blue

    flag = False
    for i in range(sx, sx+size) :
        for j in range(sy, sy+size) :
            if arr[sx][sy] != arr[i][j] :
                flag = True
                recur(sx, sy, size//2)
                recur(sx+size//2, sy, size//2)
                recur(sx, sy+size//2, size//2)
                recur(sx+size//2, sy+size//2, size//2)
                break
        if flag :
            break
    else :
        if arr[sx][sy] :
            blue += 1
        else :
            white += 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

recur(0, 0, N)
print(white)
print(blue)