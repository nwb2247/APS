"""
N, M <= 100
R <= 1000 (연산횟수)

-> 매번 진짜로 다 적용시켜도 100*100*1000 -> 시간 가능?

"""

N, M, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
ops = list(map(int, input().split()))

def op1(arr):
    return arr[::-1]

def op2(arr):
    return [lst[::-1] for lst in arr]

def op3(arr):
    return [list(lst[::-1]) for lst in zip(*arr)]

def op4(arr):
    return [list(lst) for lst in zip(*arr)][::-1]

def separate(arr):
    R = len(arr)
    C = len(arr[0])
    return ([lst[:C//2] for lst in arr[:R//2]],
            [lst[C//2:] for lst in arr[:R//2]],
            [lst[C//2:] for lst in arr[R//2:]],
            [lst[:C//2] for lst in arr[R//2:]])

def op5(arr):
    p1, p2, p3, p4 = separate(arr)
    return [p4[i] + p1[i] for i in range(len(p1))] + [p3[i] + p2[i] for i in range(len(p1))]

def op6(arr):
    p1, p2, p3, p4 = separate(arr)
    return [p2[i] + p3[i] for i in range(len(p1))] + [p1[i] + p4[i] for i in range(len(p1))]

coms = [0, op1, op2, op3, op4, op5, op6]

for op in ops:
    # for lst in arr:
    #     print(*lst, sep=" ")
    arr = coms[op](arr)

for lst in arr:
    print(*lst, sep=" ")