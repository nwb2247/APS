"""
[조건]
서로 다른 L개 알파벳 소문자,
한개 모음(a, e, i, o, u), 두 개 자음으로 구성해야함
사전순으로

C, L 모두 15 이하

[목표]
모든 경우 출력

[접근]
C, L 모두 15이하이므로, 그냥 전부 구하고, 모음이 한개 자음이 두개 이상인 경우만 출력
(L개 중에서 모음 한개 이상, 자음 두개 이상 먼저 선택하는 것이 더 까다로움, 중복 확인 등...)
입력 배열 정렬 필요!

모음의 개수 인자로 넘김 cnt
"""


def dfs(depth, start, ans, cnt):
    # 몇번째에 넣을건지, 몇번 인덱스부터 넣을 수 있는지, 정답배열, 모음의 개수

    if depth == L:
        if cnt >= 1 and L-cnt >= 2: # 모음 개수, 자음 개수 조건
            print("".join(ans))
        return

    for i in range(start, C):
        ans[depth] = lst[i]
        if lst[i] in "aeiou":
            dfs(depth + 1, i + 1, ans, cnt + 1)
        else:
            dfs(depth + 1, i + 1, ans, cnt)


L, C = map(int, input().split())
lst = list(input().split())
lst.sort()
ans = [""] * L
dfs(0, 0, ans, 0)  # (depth, start)
