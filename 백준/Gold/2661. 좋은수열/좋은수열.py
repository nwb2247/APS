"""
백트래킹, 가지치기?

"""

def isbad(depth):
    l = 1
    while depth - 2*l >= 0:
        # print(ans[:depth])
        # print(ans[depth-2*l:depth-l], ans[depth-l:depth])
        # print(ans[depth-2*l:depth-l] == ans[depth-l:depth])
        if ans[depth-2*l:depth-l] == ans[depth-l:depth]:
            return True
        else:
            l += 1
    return False

def backtracking(depth):

    global is_found

    if is_found:
        return

    if isbad(depth):
        return

    if depth == N:
        print("".join(map(str, ans)))
        is_found = True
        return

    for i in range(1, 4): # 가장 작은 수여야 하므로 되도록 1, 2, 3 순으로 넣음
        ans[depth] = i
        backtracking(depth + 1)


N = int(input())
ans = [0]*N
is_found = False
backtracking(0)

# N = 19
# lst = list(range(N))
# print(lst)
# depth = N
# l = 1
# while depth-2*l >= 0:
#     print(lst[depth-2*l:depth-l], lst[depth-l:])
#     l += 1
