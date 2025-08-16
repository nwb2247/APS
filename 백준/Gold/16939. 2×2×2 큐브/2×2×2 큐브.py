"""

"""

lll = [0] + list(map(int, input().split()))

arr = [[0, 0, 1, 2, 0, 0, 0, 0],
       [0, 0, 3, 4, 0, 0, 0, 0],
       [13, 14, 5, 6, 17, 18, 21, 22],
       [15, 16, 7, 8, 19, 20, 23, 24],
       [0, 0, 9, 10, 0, 0, 0, 0],
       [0, 0, 11, 12, 0, 0, 0, 0],
       [0, 0, 24, 23, 0, 0, 0, 0],
       [0, 0, 22, 21, 0, 0, 0, 0]]

def op1(arr):
       new_arr = [[] for _ in range(8)]
       for i in range(-2, 6):
              new_arr[i+2] = arr[i][:3] + arr[i+2][3:]
       return new_arr

def op2(arr):
       new_arr = [[] for _ in range(8)]
       for i in range(-2, 6):
              new_arr[i+2] = arr[i+2][:3] + arr[i][3:]
       return new_arr

def op3(arr):
       new_arr = [[] for _ in range(8)]
       for i in range(3):
              new_arr[i] = arr[i][:]
       for i in range(3, 8):
              new_arr[i] = arr[i][2:] + arr[i][:2]
       return new_arr

def op4(arr):
       new_arr = [[] for _ in range(8)]
       for i in range(3):
              new_arr[i] = arr[i][:]
       for i in range(3, 8):
              new_arr[i] = arr[i][-2:] + arr[i][:-2]
       return new_arr

def op5(arr):
       new_arr = [lst[:] for lst in arr]
       p = [list(lst) for lst in zip(*arr[1:5][::-1])][1:5]
       for r in range(4):
              for c in range(4):
                     new_arr[1+r][1+c] = p[r][c]
       return new_arr

def op6(arr):
       new_arr = op5(arr)
       new_arr = op5(new_arr)
       new_arr = op5(new_arr)
       return new_arr

ops = [op1, op2, op3, op4, op5, op6]
srsc = [[[0, 2, 4, 6], [0, 2, 4]],
        [[0, 2, 4, 6], [0, 2, 4]],
        [[0, 2, 4], [0, 2, 4, 6]],
        [[0, 2, 4], [0, 2, 4, 6]],
        [[0, 2, 4, 6], [0, 2, 4]],
        [[0, 2, 4, 6], [0, 2, 4]]]



def check(sr, sc):
       for r in sr:
              for c in sc:
                     if not (lll[new_arr[r][c]] ==
                             lll[new_arr[r+1][c]] ==
                             lll[new_arr[r][c+1]] ==
                             lll[new_arr[r+1][c+1]]):
                            return False
       return True

yes = False
for i, op in enumerate(ops):
       new_arr = op(arr)
       sr, sc = srsc[i]
       if check(sr, sc):
              yes = True
              break

if yes:
       print(1)
else:
       print(0)

