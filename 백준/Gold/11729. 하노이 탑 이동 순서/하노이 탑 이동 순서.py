N = int(input())

# (시작지, 도착지) -> 경유지
idle = {(1, 3): 2, (3, 1): 2,
        (2, 3): 1, (3, 2): 1,
        (1, 2): 3, (2, 1): 3}

"""
N칸짜리를 s에서 d으로 옮기려면 
일단 위 N-1칸을 s에서 남는 곳(idle)로 옮기고, 
맨아래 가장 큰 파트를 s에서 d로 옮긴후
다시 N-1짜리를 idle에서 d로 옮겨야함
"""


def recur(N, s, d):  # N: 몇칸짜리인지, s시작, d도착
    if N == 1:
        ans.append((s, d))
        return
    recur(N - 1, s, idle[(s, d)])  # 일단 위 N-1칸을 s에서 남는 곳(idle)로 옮기고                     # 맨아래 가장 큰 파트를 s에서 d로 옮긴후
    recur(1, s, d)
    recur(N - 1, idle[(s, d)], d)  # 다시 N-1짜리를 idle에서 d로 옮겨야함


cnt = 0
ans = []
recur(N, 1, 3)
print(len(ans))
for move in ans:
    print(*move)
