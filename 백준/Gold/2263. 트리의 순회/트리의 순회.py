"""
[조건]
inoder, postorder 주어지면

[목표]
 preorder로 출력

[접근]
ino =>   [--left--][p][--right--]
posto => [--left--][--right--][p]
posto에서 마지막을 p로 잡고 ino에서 p의 인덱스를 찾아 offset(p의 인덱스 - left의 시작)을 잡음

ino의 left =>    ino_s                   ~ ino_s + offset - 1
ino의 right=>    ino_s + offset + 1      ~ ino_e
posto의 left =>  posto_s                 ~ posto_s + offset - 1
posto의 right => posto_s + offset        ~ posto_e - 1

=>
[p][--left--][--right--]

"""
import sys

sys.setrecursionlimit(110000)


def preo(ino_s, ino_e, posto_s, posto_e):

    if ino_s > ino_e:
        return

    p = posto[posto_e]      # posto 범위의 마지막 : 부모 노드 p
    ino_pi = ino_idx[p]     # ino에서 부모 노드 p의 인덱스 찾음

    offset = ino_pi - ino_s
    ans.append(p)           # preorder해야하므로 부모부터
    preo(ino_s, ino_s + offset - 1, posto_s, posto_s + offset - 1)  # 왼쪽
    preo(ino_s + offset + 1, ino_e, posto_s + offset, posto_e - 1)  # 오른쪽


ans = []
N = int(input())
ino = list(map(int, input().split()))
posto = list(map(int, input().split()))
ino_idx = [0]*(N+1)                 # (D) 전처리로 인덱스 빠르게 찾기
for i, num in enumerate(ino):
    ino_idx[num] = i

preo(0, N - 1, 0, N - 1)
print(*ans)
