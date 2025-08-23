"""
디버깅
---------------------------------------------------------
[1] 90도 회전 부분
-> new_s[c][R-1-r] = s[r][c]처럼 지금 좌표가 new_s에서 어디로 찍히는지 보는게 더 편한듯

00 01 02
10 11 12

=>
   0  1
0 10 00
1 11 01
2 12 02

=> 10 11 12 가 00 10 20 이 되었음
for r in range(R):
    for c in range(C):
        new_s[c][R-1-r] = s[r][c]

[2] 시작점 정하고 거기서 패딩시켜 확인하는 부분에서
oob, 찾았으면 바로 종료, 시작점을 기억하기(br, bc) 등을 까먹었음


[3] 스티커 붙일때 스티커인 부분만 추가해야하는데 0인 부분까지 업데이트하면 틀림
"""

def oob(r, c):
    return not (0<=r<N and 0<=c<M)

def rotate(s, R, C):
    new_s = [[0]*R for _ in range(C)]
    for r in range(R):
        for c in range(C):
            new_s[c][R-1-r] = s[r][c]

    return new_s, C, R

def stick(s, R, C):
    br, bc = -1, -1
    found = False
    for sr in range(N):
        for sc in range(M):
            bad = 0
            for zr in range(R):
                for zc in range(C):
                    if oob(sr+zr, sc+zc) or (s[zr][zc] == 1 and RES[sr+zr][sc+zc] == 1):
                        bad = 1
                        break
                if bad:     # 현재 sr, sc 폐기
                    break
            if bad:         # 다음 sc 확인
                continue
            # bad 아닌데 끝까지 왔다면 break
            found = True
            br, bc = sr, sc
            break
        if found:           # 전에서 찾았다면 break
            break
    if not found:
        return False

    # return False되지 않았다면 붙일 수 있다는 것
    for zr in range(R):
        for zc in range(C):
            if s[zr][zc]:
                RES[br+zr][bc+zc] = s[zr][zc] # sr, sc아닌 br, bc 임에 주의
    return True


N, M, K = map(int, input().split())
RES = [[0]*M for _ in range(N)]     # 결과
stickers = []
for _ in range(K):
    R, C = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(R)]
    stickers.append(s)

for s in stickers:
    R = len(s)
    C = len(s[0])

    if stick(s, R, C):      # 일단 붙여보기
        continue            # 성공했으면 넘어감

    for i in range(3):      # 세번더 돌려봄
        s, R, C = rotate(s, R, C)
        if stick(s, R, C):  # 성공했으면 break
            break
    # 못붙였으면 폐기

cnt = 0
for l in RES:
    cnt += l.count(1)
print(cnt)