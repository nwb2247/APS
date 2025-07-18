import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    string = sys.stdin.readline().rstrip()
    print(string[0]+string[-1])