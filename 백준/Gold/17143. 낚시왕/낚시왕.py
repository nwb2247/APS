"""
[요약평]
1. 최적의 방법이 떠오르지 않으면, 일단 비효율적인 방법이라도 구상하자.
    답이 나오는데, 시간, 메모리 문제가 발생한다면 그 때 최적화를 진행
2. 반복적인 디버깅 출력 부분은 그냥 함수화하자 (디버깅이 길어길 것 같다면..)
3. 입력 + 출력(ans) 만 글로벌로 하고 나머지는 solve()에서 해결하자 (디버깅 수월하게 하기 위해...)

[타임라인]
이해 및 구상 15분
구현 및 디버깅 80분

[이해 및 구상]
-) 아무리 고민해봐도 움직임 방법을 깔끔하게 떠올리기 어려웠음

[구현]
-) 당초 구상했던 함수화 부분 (catch, select)를 함수화하지 않음

[디버깅]
디버깅 요소
1. 물고기를 잡고 info에서도 없애줘야했음 (3분)
2. 열방향 탐색인데 습관적으로 cr먼저 그다음 cc로 순회했음 (4분)
3. 행방향이동도 있음에도 2*C-2로만 나눔
+
4. oob 순간 바로 방향틀어서 한칸 가기때문에 2*C-2로 나눠줘야 함 (8분)

"""



# 손구상
#
# catch, move, select
# move가 관건
#
# dict로 물고기 관리 (class 처럼..)
# 이동을 한번에 하려면? (Review 구상이 잘 안됨,,,) => 제자리, 같은 방향으로 돌아오는 만큼 나눠주고 그 나머지를 하나씩 이동시키자...


ds = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}  # 위 아래 오른쪽 왼쪽
rev = {1: 2, 2: 1, 3: 4, 4: 3}      # 역방향


def oob(r, c):
    return not (0 <= r < R and 0 <= c < C)

# 물고기들 움직이는 로직
def move():
    # for l in arr:     (D) 자주 쓰이므로 디버깅용으로 함수화 하는게 좋을듯
    #     print(l)
    # print(info)
    for b, v in info.items():   # 각 물고기에 대해서

        # [1] 물고기 꺼내기
        cr, cc, s, cd = v       # 물고기를 꺼내고
        arr[cr][cc].remove(b)   # 지도에서도 물고기 없앰

        # [2] 물고기 새 위치 구하기
        if cd == 1 or cd == 2:      # 세로 방향이면 (2 * R - 2) 로 나누기
            mod = s % (2 * R - 2)
        else:
            mod = s % (2 * C - 2)   # 가로 방향이면 (2 * R - 2) 로 나누기
            
        for i in range(mod):        # mod의 양만큼 돌기
            dr, dc = ds[cd]
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc):         # 범위를 넘어가는 순간, 제자리에서 반대방향으로 한칸 감
                cd = rev[cd]
                dr, dc = ds[cd]
                nr, nc = cr + dr, cc + dc
            cr, cc = nr, nc

        # [3] 새로 구한 위치로 다시 업데이트 (info, arr 모두)
        info[b] = (cr, cc, s, cd)
        arr[cr][cc].add(b)

R, C, K = map(int, input().split())
arr = [[set() for _ in range(C)] for _ in range(R)]
info = dict()
for _ in range(K):  # 모든 물고기 크기 다르므로 id 대신 b 사용
    r, c, s, d, b = map(int, input().split())  # r, c, 스피드, 방향, 크기
    info[b] = (r - 1, c - 1, s, d)  # 좌표랑 1씩 빼줘야함
    arr[r - 1][c - 1].add(b)

ans = 0
for cc in range(C):  # (D) cr, cc 순서 바뀜
    # [1] 채취
    for cr in range(R):
        if arr[cr][cc]:
            b = arr[cr][cc].pop()  # 어차피 한개
            info.pop(b)  # (D) info에서도 지워야함
            ans += b
            break

    # print("채취")
    # print(info)
    # for l in arr:
    #     print(l)

    # [2] 이동
    move()

    # print("이동")
    # print(info)
    # for l in arr:
    #     print(l)

    # [3] 한마리만 살리기
    for zr in range(R):
        for zc in range(C):
            if len(arr[zr][zc]) <= 1:   # 1마리거나 0마리면 넘어감
                continue
            # [3-1] 가장 큰 것 찾음
            mx = max(arr[zr][zc])
            # [3-2] 가장 큰것 외에 나머지는 info에서 먼저 지움
            removed = []                # 나중에 arr에서도 지워야하므로 removed에 저장
            for k in arr[zr][zc]:
                if k == mx:             # 가장 큰건 넘어감
                    continue
                info.pop(k)  # info에서 지우기
                removed.append(k)
            # [3-3] arr에서도 지움
            for k in removed:  # arr에서 지우기
                arr[zr][zc].remove(k)

print(ans)


# # 리팩토링, 한번에 이동
# ds = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}  # 위 아래 오른쪽 왼쪽
#
# 
# R, C, K = map(int, input().split())
# arr = [[set() for _ in range(C)] for _ in range(R)]  # 어떤 물고기가 들어있는지
# info = dict()  # 각 물고기의 정보, b를 일종의 식별자로 사용 (크기가 겹치는 물고기가 없으므로...)
# for _ in range(K):  # 모든 물고기 크기 다르므로 id 대신 b 사용
#     r, c, s, d, b = map(int, input().split())  # r, c, 스피드, 방향, 크기
#     info[b] = (r - 1, c - 1, s, d)  # 좌표 1씩 빼줘야함
#     arr[r - 1][c - 1].add(b)  # arr에도 반영
# 
# 
# def oob(r, c):
#     return not (0 <= r < R and 0 <= c < C)
# 
# 
# def catch(cc):  # 잡기
#     global ans
#     for cr in range(R):  # 위에서부터 확인
#         if arr[cr][cc]:
#             b = arr[cr][cc].pop()  # 어차피 한개 (없으면 에러)
#             info.pop(b)  # info에서도 지워야함
#             ans += b
#             break
# 
# 
# rev = {1: 2, 2: 1, 3: 4, 4: 3}  # 역방향
# bounds = {1: (0, R - 1), 2: (R - 1, 0), 3: (C - 1, 0),
#           4: (0, C - 1)}  # first_bound, second_bound (처음부딪히는 벽), (두번째 부딪히는 벽)
# 
# 
# def next_pos(cr, cc, s, cd):  # 각 물고기 별로 다음 좌표를 계산
#     if cd in {1, 2}:
#         cur, mod, axis = cr, s % (2 * R - 2), 0  # 현재 위치, 2*(움직일 방향에 대한 배열의 길이) -2 로 s를 나눈값, cur이 어느 축을 기준으로 하는지
#     else:  # 3, 4
#         cur, mod, axis = cc, s % (2 * C - 2), 1
# 
#     fb, sb = bounds[cd]
#     if mod <= abs(fb - cur):  # 첫번째 벽 만나기 전에 끝나면
#         nxt = cur + ds[cd][axis] * mod
#         nd = cd
#     elif mod <= abs(fb - cur) + abs(fb - sb):  # 두번째 벽 만나기 전에 끝나면
#         nxt = fb + ds[rev[cd]][axis] * (mod - abs(fb - cur))
#         nd = rev[cd]
#     else:  # 두번째 벽까지 부딪힌다면
#         nxt = sb + ds[cd][axis] * (mod - (abs(fb - cur) + abs(fb - sb)))
#         nd = cd
# 
#     if axis == 0:  # 세로로 움직이면
#         return nxt, cc, nd
#     else:  # 가로로 움직이면
#         return cr, nxt, nd
# 
# 
# def move():
#     for b in info:
#         cr, cc, s, cd = info[b]  # 각 물고기의 정보 가져옴
#         # [1] arr의 원래 위치에서 지움
#         arr[cr][cc].remove(b)
#         # [2] 다음 위치를 구하고 업데이트
#         nr, nc, nd = next_pos(cr, cc, s, cd)
#         info[b] = (nr, nc, s, nd)
#         # [3] arr에 새롭게 반영
#         arr[nr][nc].add(b)
# 
# 
# def select():      # 한마리만 살리기
#     for zr in range(R):
#         for zc in range(C):
#             if len(arr[zr][zc]) <= 1:   # 1마리거나 0마리면 넘어감
#                 continue
#             # [1] 가장 큰 것 찾음
#             mx = max(arr[zr][zc])
#             # [2] 가장 큰것 외에 나머지는 info에서 먼저 지움
#             removed = []                # 나중에 arr에서도 지워야하므로 removed에 저장
#             for k in arr[zr][zc]:
#                 if k == mx:             # 가장 큰건 넘어감
#                     continue
#                 info.pop(k)  # info에서 지우기
#                 removed.append(k)
#             # [3] arr에서도 지움
#             for k in removed:  # arr에서 지우기
#                 arr[zr][zc].remove(k)
# 
# ans = 0
# def solve():
#     for cc in range(C):  # (D) cr, cc 순서 바뀜
#         # [1] 채취
#         catch(cc)
#         # [2] 이동
#         move()
#         # [3] 한마리만 남기기
#         select()
# 
# 
# solve()
# 
# print(ans)
