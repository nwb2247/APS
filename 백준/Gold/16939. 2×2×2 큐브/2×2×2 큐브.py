"""
3차원 * 차원마다 돌리는 방향 두개 
    -> 6가지 방법 존재
한 방법씩 수행하고, 면마다 모든 칸의 색이 일치하게 되면 1출력 아니면 0출력

큐브의 표현 -> 2차원 전개도
회전 방법 -> 2차원 전개도 상에서 좌표를 이동시켜줌
"""

INFO = [0] + list(map(int, input().split()))  # 1부터 시작하도록 패딩 (0은 빈 인덱스를 의미하도록)

ARR = [[0, 0, 1, 2, 0, 0, 0, 0],  # 각 인덱스 위치를 2차원에 표현
       [0, 0, 3, 4, 0, 0, 0, 0],
       [13, 14, 5, 6, 17, 18, 21, 22],
       [15, 16, 7, 8, 19, 20, 23, 24],
       [0, 0, 9, 10, 0, 0, 0, 0],
       [0, 0, 11, 12, 0, 0, 0, 0],
       [0, 0, 24, 23, 0, 0, 0, 0],  # 세로로 돌리는 경우 (op0, op1) 위해서
       [0, 0, 22, 21, 0, 0, 0, 0]]  # 아래쪽에도 21~24에 해당하는 면을 작성

# op0,1,2,3: 슬라이싱 기반 돌리기, op4,5: 인덱스 기반 돌리기 (90도)

def op0(arr):  # 5, 7을 위로 돌리기
    new_arr = [lst[:] for lst in arr]  # 깊은 복사
    for i in range(8):
        new_arr[i - 2][:3] = arr[i][:3]
    return [lst[:6] for lst in new_arr]  # 아래쪽 21~24를 사용하므로 5열까지 반환


def op1(arr):  # 5, 7을 아래로 돌리기
    new_arr = [lst[:] for lst in arr]  # 깊은 복사
    for i in range(8):
        new_arr[i][:3] = arr[i - 2][:3]
    return [lst[:6] for lst in new_arr]  # 아래쪽 21~24를 사용하므로 5열까지 반환


def op2(arr):  # 5, 6을 오른쪽으로 돌림
    new_arr = [lst[:] for lst in arr]  # 깊은 복사
    for i in range(3):
        new_arr[i] = arr[i][-2:] + arr[i][:-2]
    return new_arr[:6]  # 오른쪽 21~24를 사용하므로 5행까지 반환


def op3(arr):  # 5, 6을 왼쪽으로 돌림
    new_arr = [lst[:] for lst in arr]  # 깊은 복사
    for i in range(3):
        new_arr[i] = arr[i][2:] + arr[i][:2]
    return new_arr[:6]  # 오른쪽 21~24를 사용하므로 5행까지 반환


def op4(arr):  # 5~8 중심으로  4*4범위 시계방향 90도
    new_arr = [lst[:] for lst in arr]  # 깊은 복사
    for r in range(1, 5):
        for c in range(1, 5):
            new_arr[r][c] = arr[5-c][r] # 새로운 좌표 r, c가 arr에 어떻게 대응되는지 생각하기
    return new_arr[:6]  # 오른쪽 21~24를 사용하기 5행까지 반환 (아래로 해도 상관X)


def op5(arr):  # 5~8 중심으로  4*4범위 반시계방향 90도
    new_arr = [lst[:] for lst in arr]  # 깊은 복사
    for r in range(1, 5):
        for c in range(1, 5):
            new_arr[r][c] = arr[c][5-r] # 새로운 좌표 r, c가 arr에 어떻게 대응되는지 생각하기
    return new_arr[:6]  # 오른쪽 21~24를 사용하기 5행까지 반환 (아래로 해도 상관X)


ops = [op0, op1, op2, op3, op4, op5]

# # 제대로 돌아가는지 확인 (디버깅)
# for i in range(6):
#     NEW_ARR = ops[i](ARR)
#     print(f"op{i}")
#     for l in NEW_ARR:
#         print(l)
#     print()


def check(new_arr):  # 각 6면이 일치하는지 확인 (빈공간은 0인덱스인데, INFO[0] == 0으로 항상 모두 같은 색으로 인식)
    R = len(new_arr)        # 행의 길이
    C = len(new_arr[0])     # 열의 길이
    for r in range(0, R, 2):
        for c in range(0, C, 2):
            if not (INFO[new_arr[r][c]] ==  # 하나라도 틀린게 있으면 False 반환
                    INFO[new_arr[r + 1][c]] ==
                    INFO[new_arr[r][c + 1]] ==
                    INFO[new_arr[r + 1][c + 1]]):
                return False
    return True  # 모든 면 색 동일하면 True 반환


def solve():
    for i in range(6): # 각 돌리는 방향에 대해
        new_arr = ops[i](ARR)  
        if check(new_arr):  # 모든 면이 맞춰졌으면 1반환
            return 1
    return 0                # 아니면 0 반환


print(solve())
