"""
[p][---left---][---right---]
[---left---][---right---][p]

이진탐색이용해서 p보다 작은 값중 가장 오른쪽에 있는 인덱스를 선택 -> 거기까지가 left
"""
import sys
sys.setrecursionlimit(10000)

st = sys.stdin.readline()
LIST = []
while st != "":
    LIST.append(int(st))
    st = sys.stdin.readline()

def postorder(s, e):
    if s == e:
        print(LIST[s])
        return

    p = LIST[s]
    if LIST[s + 1] > p:  # LIST가 전위이므로 길이가 1이 아니라면 s+1은 항상 범위내에 있음
        postorder(s + 1, e)
    else:
        l, r = s + 1, e
        while l <= r:
            m = (l + r) // 2
            if LIST[m] < p:
                end_of_left = m
                l = m+1
            else:
                r = m-1
        postorder(s+1, end_of_left)
        if end_of_left + 1 <= e:
            postorder(end_of_left+1, e)
    print(p)

postorder(0, len(LIST)-1)
