def preorder(cur):
    global ans_pre
    if cur == -1:
        return
    ans_pre += to_char(cur)
    preorder(left[cur])
    preorder(right[cur])

def inorder(cur):
    global ans_in
    if cur == -1:
        return
    inorder(left[cur])
    ans_in += to_char(cur)
    inorder(right[cur])

def postorder(cur):
    global ans_post
    if cur == -1:
        return
    postorder(left[cur])
    postorder(right[cur])
    ans_post += to_char(cur)


def to_int(char):
    return ord(char)-ord("A")

def to_char(num):
    return chr(num+ord("A"))

N = int(input())
left = [-1]*26
right = [-1]*26
for _ in range(N):
    tlst = list(input().split())
    p = to_int(tlst[0])
    if tlst[1] != ".":
        left[p] = to_int(tlst[1])
    if tlst[2] != ".":
        right[p] = to_int(tlst[2])

ans_pre = ""
ans_in = ""
ans_post = ""
preorder(0)
inorder(0)
postorder(0)
print(ans_pre)
print(ans_in)
print(ans_post)

