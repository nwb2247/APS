import sys

strings = []
maxLen = 0
for _ in range(5) :
    s = sys.stdin.readline().rstrip()
    maxLen = max(maxLen, len(s))
    strings.append(s)
output = []
for i in range(maxLen) :
    for j in range(5) :
        if i < len(strings[j]) :
            output.append(strings[j][i])
print("".join(output))