"""
두공 사이의 간격 짝수 : 움직이는 순서에 따라 영향 없다
하나씩 움직이고 닿는 순간 둘다 방향 바꿔주기?
L 1000
N 공의 개수 100
T 시간 1000

M*N*T 100_000_000
구해야하는 것 : 몇번 충돌하는가

다음거 확인하고 벽에 부딪히면 방향전환 벽 아닌데, 공 잇으면 둘다 바꿔줌
벽부터 시작하는 입력은 없음.
"""
L, N, T = map(int, input().split())
box = [[] for _ in range(L+1)]        # 각 위치에 리스트 만들고 여러개 동시에 오는 공 처리
# 0, L이 벽 위치
balls = [[0,0] for _ in range(N)]# 위치, 방향 (-1 왼쪽 1 오른쪽
for i in range(N): # i 공의 번호
    inp = input().split()
    pos = int(inp[0])
    d = 1 if inp[1] == "R" else -1

    balls[i] = [pos, d]    # 값이 계속 바뀌므로 list로
    box[pos].append(i)        # 해당 위치에 다른 공에 존재하면 둘다 바꿔주도록...

"""
공마다 다 이동시키고 박스에 반영, 
다시 공마다 위치 확인하면서 두개 이상있거나 벽이라면, visited 배열 이용해서, 처리된건 pass (두번 처리되지 않도록)
"""
# print(box, balls)
t = 0
cnt = 0
while t<T:
    for i in range(N):
        pos, d = balls[i]
        npos = pos+d    # 다음위치
        box[pos].remove(i)  # 박스에서 원래 위치에서 인덱스 제거, 다음 위치에 append
        box[npos].append(i)
        balls[i][0] = npos # 박스에도 반영

    visited = [0]*N
    for i in range(N):
        pos, d = balls[i]
        if visited[i] == 1:
            continue    # 이미 처리가 이뤄졌다면 넘어감
        if pos == 0 or pos == L:
            balls[i][1] *= -1  # 위치 반대방향으로 바꿔줌
        elif len(box[pos]) >= 2:
            for idx in box[pos]:
                balls[idx][1] *= -1 # 위치 반대방향으로 바꿔줌
                visited[idx] = 1
            cnt += 1
    t += 1
    # print(cnt)
    # print(t, box, balls)
print(cnt)


