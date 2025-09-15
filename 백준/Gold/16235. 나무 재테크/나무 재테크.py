"""
N*N
1, 1부터 시작

같은 칸에 여러 나무가 심어져 있을 수도 있음

처음에 양분은 5만큼 들어있음

봄
하나의 칸에 여러 나무가 있다면 어린 나무부터 양분을 먹음, 양분이 부족해 자기 나이만큼 양분을 못먹으면 즉시 죽음

여름
봄에 죽은 나무가 양분으로 변함, 각 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가

가을
나무가 번식 나이가 5의 배수면 인접한 8개 칸에 나이가 1인 나무가 생김, oob엔 안생김

겨울
A[r][c] 만큼 양분을 추가

K년이 지난 후 살아 있는 나무의 개수 구하기

"""

DEBUG = 0

def dprint(st):
    if DEBUG:
        print(st)
        for l in trees:
            print(l)
        for l in nut:
            print(*l)
        print()

def oob(r, c):
    return not (0<=r<N and 0<=c<N)

def spring():
    dead = []
    for cr in range(N):
        for cc in range(N):
            trees[cr][cc].sort()  # 어린 나무부터 양분주기 위해서 오름차순 정렬
            tmp = []
            for t in trees[cr][cc]:
                if nut[cr][cc] >= t:  # 남은 양분이 나무 나이보다 많거나 같다면
                    nut[cr][cc] -= t
                    tmp.append(t + 1)   #  한살 더해줌
                else:
                    dead.append((cr, cc, t))  # 충분하지 않다면 죽임
            trees[cr][cc] = tmp  # tmp를 trees에 갱신

    return dead


def summer(dead):
    for cr, cc, m in dead:
        nut[cr][cc] += m // 2   # 소수점은 버리고 //2한 값이 양분이 됨

    return


def fall():
    babies = [[0 for _ in range(N)] for _ in range(N)]  # 각 위치에 추가될 아기 나무의 개수
    for cr in range(N):
        for cc in range(N):
            for t in trees[cr][cc]:
                if t%5 == 0:
                    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        nr, nc = cr+dr, cc+dc
                        if oob(nr, nc): # (D) oob에서는 번식 불가
                            continue
                        babies[nr][nc] += 1
    for cr in range(N):
        for cc in range(N):
            trees[cr][cc].extend([1]*babies[cr][cc])

    return


def winter():
    for cr in range(N):
        for cc in range(N):
            nut[cr][cc] += A[cr][cc]
    return


def solve():
    for t in range(K):

        if DEBUG:
            print("----------------------------------------------------")

        dead = spring()
        dprint(f"{t} 봄")

        summer(dead)
        dprint(f"{t} 여름")

        fall()
        dprint(f"{t} 가을")

        winter()
        dprint(f"{t} 겨울")


    cnt = 0
    for cr in range(N):
        for cc in range(N):
           cnt += len(trees[cr][cc])
    print(cnt)

    return

N, M, K = map(int, input().split())  # M:나무의 개수, K년이 지난 후 나무의 개수
A = [list(map(int, input().split())) for _ in range(N)]
nut = [[5 for _ in range(N)] for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    X, Y, Z = map(int, input().split())
    trees[X - 1][Y - 1].append(Z)

solve()
