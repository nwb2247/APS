import sys

r, c = map(int, sys.stdin.readline().split())

mine = [[True for _ in range(c)] for _ in range(r)]
left_descending = [[-1 for _ in range(c)] for _ in range(r)]
right_descending = [[-1 for _ in range(c)] for _ in range(r)]

for y in range(r) :
    x = 0
    for i in map(int, list(sys.stdin.readline().strip())) :
        if not(i) :
            mine[y][x] = False
        x += 1

for y in range(r) :
    for x in range(c) :

        ## right_descending
        if right_descending[y][x] != -1 :
            rd = right_descending[y][x]
        else :
            v = 0
            while x+v <= c-1 and y+v <= r-1 :
                if mine[y+v][x+v] :
                    v += 1                   
                else : break

            if v == 0 :
                right_descending[y][x] = 0
            else :
                for i in range(v) :
                    right_descending[y+i][x+i] = v-i

        ## left_descending
        if left_descending[y][x] != -1 :
            rd = left_descending[y][x]
        else :
            v = 0
            while x-v >= 0 and y+v <= r-1 :
                if mine[y+v][x-v] :
                    v += 1                   
                else : break
            if v == 0 :
                left_descending[y][x] = 0
            else :
                for i in range(v) :
                    left_descending[y+i][x-i] = v-i

limit_n = int(min(r, c) / 2 + 1)
max_n = 0

for y in range(r) :
    for x in range(c) :
        cur_n = min([left_descending[y][x], right_descending[y][x], limit_n])

        if cur_n <= max_n :
            continue

        curmax_n = 0
        for n in range(cur_n, 0, -1) :
            if min(left_descending[y+(n-1)][x+(n-1)], right_descending[y+(n-1)][x-(n-1)]) >= n :
                curmax_n = n
                break
        if curmax_n > max_n :
            max_n = curmax_n

print(max_n)