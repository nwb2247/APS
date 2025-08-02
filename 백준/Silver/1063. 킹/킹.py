"""

[목표]
킹과 돌의 마지막 위치 출력

[조건]
알파벳 열, 숫자 행
행은 위로 올라갈수록 숫자도 커짐 (1부터 시작)

!!! 킹이 이동할 자리에 돌이 있다면, 돌을 킹이 움직인 방향으로 옮겨줌
돌이나 킹이 체스판 밖으로 나가는 경우는 무효

[접근]
1 킹이 이동할 자리가 범위 내에 있다면
    11 그 자리에 돌이 있다면
        101 돌이 이동할 자리가 범위 내에 있다면
            둘다 옮김
        100
            X (무효)
    10 (그 자리에 돌이 없다면)
        옮김
0               => 생략 가능
    X (무효)

to_char, to_num 구현

[엣지케이스]

[주의]
행은 위로 올라갈수록 숫자도 커짐 (1부터 시작)
통일성 위해 A도 1부터 시작하도록 하기
"""


def to_num(char):  # A -> 1에 대응되도록
    return ord(char) - ord("A") + 1


def to_char(num):
    return chr(num - 1 + ord("A"))


ds = {"R": [0, 1], "L": [0, -1], "B": [-1, 0], "T": [1, 0]}
king, stone, Nst = input().split()

kr = int(king[1])
kc = to_num(king[0])
zr = int(stone[1])
zc = to_num(stone[0])
N = int(Nst)

ops = [input().rstrip() for _ in range(N)]

for op in ops:  # "LT"
    ndr, ndc = 0, 0
    for char in op:  # "L" / "T":
        dr, dc = ds[char]
        ndr += dr
        ndc += dc

    nkr, nkc = kr + ndr, kc + ndc
    if 1 <= nkr <= 8 and 1 <= nkc <= 8:
        if nkr == zr and nkc == zc:     # (debug) : and를 써야 하는데 or을 씀;;;;
            nzr, nzc = zr + ndr, zc + ndc
            if 1 <= nzr <= 8 and 1 <= nzc <= 8:
                kr, kc = nkr, nkc
                zr, zc = nzr, nzc
            else:
                continue
        else:
            kr, kc = nkr, nkc
    else: # 생략 가능
        continue

print(to_char(kc)+str(kr))
print(to_char(zc)+str(zr))
