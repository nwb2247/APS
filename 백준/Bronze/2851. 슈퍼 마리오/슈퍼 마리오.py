lst = [int(input()) for _ in range(10)]
sol = lst[0]
for i in range(1, 10) :
    lst[i] = lst[i-1]+lst[i]
    a = abs(lst[i]-100) - abs(sol - 100)
    if a<0 or (a==0 and lst[i]>sol) :
        sol = lst[i]
print(sol)
