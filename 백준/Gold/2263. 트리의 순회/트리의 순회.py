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

    if ino_s > ino_e:
        return

    p = posto[posto_e]
    ino_pi = ino_idx[p]
    # 주의 : [ino_s:ino_e+1]에서만 찾지 않으면 시간 터짐

    offset = (ino_pi - 1) - ino_s
    ans.append(p)
    preo(ino_s, ino_s + offset, posto_s, posto_s + offset)
    preo(ino_s + offset + 2, ino_e, posto_s + offset + 1, posto_e - 1)


ans = []
N = int(input())
ino = list(map(int, input().split()))
posto = list(map(int, input().split()))
ino_idx = [0]*(N+1)
for i, num in enumerate(ino):
    ino_idx[num] = i

preo(0, N - 1, 0, N - 1)
print(*ans)
