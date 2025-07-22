lst = input().split("-")
for i in range(len(lst)):
    lst[i] = sum(map(int, lst[i].split('+')))
for i in range(1, len(lst)):
    lst[i] *= -1
print(sum(lst))
