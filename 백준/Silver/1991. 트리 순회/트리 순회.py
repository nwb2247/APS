def preorder(cur):
    lc = children[cur][0]
    rc = children[cur][1]
    pre_ans.append(chr(cur + ord("A")-1))
    if lc != 0:
        preorder(lc)
    if rc != 0:
        preorder(rc)


def inorder(cur):
    lc = children[cur][0]
    rc = children[cur][1]
    if lc != 0:
        inorder(lc)
    in_ans.append(chr(cur + ord("A")-1))
    if rc != 0:
        inorder(rc)


def postorder(cur):
    lc = children[cur][0]
    rc = children[cur][1]
    if lc != 0:
        postorder(lc)
    if rc != 0:
        postorder(rc)
    post_ans.append(chr(cur + ord("A")-1))


N = int(input())
children = [[0,0] for _ in range(N+1)]
pre_ans = []
in_ans = []
post_ans = []

for _ in range(N):
    pp, ll, rr = map(lambda x: ord(x)-ord("A")+1 if x!="." else 0, input().split())
    children[pp][0] = ll
    children[pp][1] = rr

preorder(1)
inorder(1)
postorder(1)
print("".join(pre_ans))
print("".join(in_ans))
print("".join(post_ans))



