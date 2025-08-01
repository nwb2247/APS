"""
신호등 dict에 넣고,
시간을 (r+g) 나눈 나머지에 대해서 r보다 작으면 빨간, r보다 크거나 같으면 초록
"""

N, L = map(int, input().split())

lights = dict()
for _ in range(N):
    D, R, G = map(int, input().split())
    lights[D] = (R, G)
l = 0
sec = 0
while l<L:
    if l in lights.keys():
        r, g = lights[l]
        if sec%(r+g) < r:
            l += 1
            sec += r-sec%(r+g)+1
        else:
            l += 1
            sec += 1
    else:
        l += 1
        sec += 1
print(sec)


