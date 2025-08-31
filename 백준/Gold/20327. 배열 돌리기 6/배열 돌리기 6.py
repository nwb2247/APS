N, K = map(int, input().split())
R, C = 2**N, 2**N
arr = [list(map(int, input().split())) for _ in range(R)]
ops = [None]*K
for i in range(K):
    k, l = map(int, input().split())
    ops[i] = (k, l)

topleft = [[] for _ in range(N)] # 0<=l<N
for l in range(N):
    for i in range(0, R//(2**l)):
        for j in range(0, C//(2**l)):
            topleft[l].append((i*(2**l), j*(2**l)))

def op1(l):
    tmp = []
    for sr, sc in topleft[l]:
        br = sr-1
        offset_r = 2**l+1
        for cr in range(sr, sr+2**l):
            for cc in range(sc, sc+2**l):
                dr = cr - br
                nr, nc = br - dr + offset_r, cc
                tmp.append((nr, nc, arr[cr][cc]))
    for nr, nc, val in tmp:
        arr[nr][nc] = val

def op2(l):
    tmp = []
    for sr, sc in topleft[l]:
        bc = sc-1
        offset_c = 2**l+1
        for cr in range(sr, sr+2**l):
            for cc in range(sc, sc+2**l):
                dc = cc-bc
                nr, nc = cr, bc - dc + offset_c
                tmp.append((nr, nc, arr[cr][cc]))
    for nr, nc, val in tmp:
        arr[nr][nc] = val

def op3(l):
    tmp = []
    for sr, sc in topleft[l]:
        br, bc = sr-1, sc-1
        offset_c = 2**l+1
        for cr in range(sr, sr+2**l):
            for cc in range(sc, sc+2**l):
                dr, dc = cr-br, cc-bc # (D) br-cr
                nr, nc = br + dc, bc - dr + offset_c
                tmp.append((nr, nc, arr[cr][cc]))
    for nr, nc, val in tmp:
        arr[nr][nc] = val

def op4(l):
    tmp = []
    for sr, sc in topleft[l]:
        br = sr-1
        bc = sc-1
        offset_r = 2**l+1
        for cr in range(sr, sr+2**l):
            for cc in range(sc, sc+2**l):
                dr, dc = cr-br, cc-bc
                nr, nc = br-dc+offset_r, bc+dr
                tmp.append((nr, nc, arr[cr][cc]))
    for nr, nc, val in tmp:
        arr[nr][nc] = val

def op5(l):
    tmp = []
    br = -1
    offset_r = R+1 -(2**l - 1)
    for sr, sc in topleft[l]:
        dsr = sr-br
        nsr = br-dsr+offset_r
        for i in range(2**l):
            for j in range(2**l):
                tmp.append((nsr+i, sc+j, arr[sr+i][sc+j]))
    for nr, nc, val in tmp:
        arr[nr][nc] = val

def op6(l):
    tmp = []
    bc = -1
    offset_c = C+1-(2**l-1)
    for sr, sc in topleft[l]:
        dsc = sc-bc
        nsc = bc-dsc+offset_c
        for i in range(2**l):
            for j in range(2**l):
                tmp.append((sr+i, nsc+j, arr[sr+i][sc+j]))
    for nr, nc, val in tmp:
        arr[nr][nc] = val

def op7(l):
    tmp = []
    br, bc = -1, -1
    offset_c = C+1 - (2**l-1)
    for sr, sc in topleft[l]:
        dsr, dsc = sr-br, sc-bc
        nsr, nsc = br+dsc, bc-dsr+offset_c
        for i in range(2**l):
            for j in range(2**l):
                tmp.append((nsr+i, nsc+j, arr[sr+i][sc+j]))
    for nr, nc, val in tmp:
        arr[nr][nc] = val

def op8(l):
    tmp= []
    br, bc = -1, -1
    offset_r = R+1 - (2**l-1)
    for sr, sc in topleft[l]:
        dsr, dsc = sr-br, sc-bc
        nsr, nsc = br-dsc+offset_r, bc+dsr
        for i in range(2**l):
            for j in range(2**l):
                tmp.append((nsr+i, nsc+j, arr[sr+i][sc+j]))
    for nr, nc, val in tmp:
        arr[nr][nc] = val

oplst = [None, op1, op2, op3, op4, op5, op6, op7, op8]

for k, l in ops:
    oplst[k](l)

for l in arr:
    print(*l)
