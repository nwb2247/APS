"""
두손 동시에 못움직임
자음 모음 따로따로 (한글 기준)
but 입력은 알파벳 소문자로 주어짐
시간은 직전 위치와의 맨하탄 거리
누르는데에도 1의 시간이 걸림
"""


def is_left(c):
    return c in "qwertasdfgzxcv"


keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
to_pos = {}
for r in range(3):
    for c in range(len(keyboard[r])):
        to_pos[keyboard[r][c]] = (r, c)

cl, cr = input().split()
chars = input()

cnt = 0
for char in chars:
    cnt += 1  # 누르는 시간
    if is_left(char):
        ci, cj = to_pos[cl]
        ni, nj = to_pos[char]
        cnt += abs(ci - ni) + abs(cj - nj)
        cl = char
    else:
        ci, cj = to_pos[cr]
        ni, nj = to_pos[char]
        cnt += abs(ci - ni) + abs(cj - nj)
        cr = char
print(cnt)
