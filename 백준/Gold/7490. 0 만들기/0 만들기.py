"""
백트래킹

출력시 아스키 순으로 정렬 필요 set에 넣고, list화 하고 정렬?

한칸 띄우고 출력해야함!!!!!!!

+, - , " "을 가지고 넣 뺗 해서 마지막에 0된느지 확인
N-1개 넣기

"""
ops = ["+", "-", " "]

def cal():
    ret = "1"
    res = "1"
    for i in range(N-1):
        if ans[i] == " ":
            ret += str(i+2)
        else:
            ret += (ans[i]+str(i+2))
        res += (ans[i]+str(i+2))

    if eval(ret) == 0:
        sset.add(res)


def backtrack(depth):

    if depth == N-1: #N아님주의!!!!!
        cal()
        return

    for op in ops:
        ans[depth] = op
        backtrack(depth+1)

TC = int(input())

for _ in range(1, TC+1):
    sset = set()
    N = int(input())
    ans = [""]*(N-1)
    backtrack(0)

    lst = list(sset)
    lst.sort()
    print(*lst, sep="\n")
    print()