import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(min(nums), max(nums))