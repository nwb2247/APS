"""
[조건]
inoder, postorder 주어지면

[목표]
 preorder로 출력

[접근]
[--left--][p][--right--]
[--left--][--right--][p]
posto에서 마지막을 p로 잡고
=>
[p][--left--][--right--]

"""
import sys

sys.setrecursionlimit(110000)


def preo(ino_s, ino_e, posto_s, posto_e):
    if ino_s == ino_e:
        ans.append(ino[ino_s])
        return
    elif ino_s > ino_e:
        return

    p = posto[posto_e]
    for ino_pi in range(ino_s, ino_e+1):
        if ino[ino_pi] == p:
            break
    # 주의 : [ino_s:ino_e+1]에서만 찾지 않으면 시간 터짐

    left_ino_s = ino_s
    left_ino_e = ino_pi - 1
    left_posto_s = posto_s
    left_posto_e = posto_s + (left_ino_e - left_ino_s)

    right_ino_s = left_ino_e + 2
    right_ino_e = ino_e
    right_posto_s = left_posto_e + 1
    right_posto_e = posto_e - 1

    ans.append(p)

    # print(ans)
    preo(left_ino_s, left_ino_e, left_posto_s, left_posto_e)
    preo(right_ino_s, right_ino_e, right_posto_s, right_posto_e)





ans = []
N = int(input())
# N = 100000
ino = list(map(int, input().split()))
# ino = list(range(1, N+1))
posto = list(map(int, input().split()))
# posto = list(range(N, -1, -1))
preo(0, N - 1, 0, N - 1)
print(*ans)
