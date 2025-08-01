N, M = map(int, input().split())
q_inp = list(map(int, input().split()))
q_num = q_inp[0]
q_lst = [[0, 0] for _ in range(q_num)]
for i in range(q_num):
    q_lst[i] = [q_inp[2 * i + 1] - 1, q_inp[2 * i + 2] - 1]
k_inp = list(map(int, input().split()))
k_num = k_inp[0]
k_lst = [[0, 0] for _ in range(k_num)]
for i in range(k_num):
    k_lst[i] = [k_inp[2 * i + 1] - 1, k_inp[2 * i + 2] - 1]
p_inp = list(map(int, input().split()))
p_num = p_inp[0]
p_lst = [[0, 0] for _ in range(p_num)]
for i in range(p_num):
    p_lst[i] = [p_inp[2 * i + 1] - 1, p_inp[2 * i + 2] - 1]

placed = [[0] * M for _ in range(N)]
safe = [[1] * M for _ in range(N)]
for r, c in q_lst:
    placed[r][c] = 1
    safe[r][c] = 0
for r, c in k_lst:
    placed[r][c] = 1
    safe[r][c] = 0
for r, c in p_lst:
    placed[r][c] = 1
    safe[r][c] = 0

for r, c in k_lst:
    for dr, dc in [[-2, -1], [-1, -2], [2, 1], [1, 2], [-2, 1], [-1, 2], [2, -1], [1, -2]]:
        if 0 <= r+dr < N and 0 <= c+dc < M:
            safe[r + dr][c + dc] = 0
for r, c in q_lst:
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
        k = 1
        while 0 <= r+dr * k < N and 0 <= c+dc * k < M:
            if placed[r + dr * k][c + dc * k] == 1:
                break
            safe[r + dr * k][c + dc * k] = 0
            k += 1
sm = 0
for lst in safe:
    sm += sum(lst)
print(sm)

# for lst in safe:
#     print(lst)
# print()
# for lst in placed:
#     print(lst)
