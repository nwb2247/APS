import sys

# order = 0
# m = 0
# for i in range(1, 10) :
#      n = int(sys.stdin.readline())
#      if n > m :
#          m = n
#          order = i
# print(m)
# print(order)
nums = []
for n in range(9) :
    nums.append(int(sys.stdin.readline()))
m = max(nums)
print(m)
print(nums.index(m)+1)