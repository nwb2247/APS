# 10809

import sys
input = sys.stdin.readline

alph_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input().rstrip()
l = [text.find(a) for a in alph_list]
print(" ".join(list(map(str, l))))